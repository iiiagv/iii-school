import socket
import struct
import time
import logging
import threading
import json
import datetime

import agv_timer
import agv_consts
import agv_acmp
import agv_mission
import agv_sqlite

logger = logging.getLogger("Client")


class TcpClient:

    def __init__(self, host, port):

        self.host            = host
        self.port            = int(port)

        self._sock_error     = False
        self._sock_safe_lock = threading.Lock()
        self._sock           = self.connect()

        self.idle_timer      = agv_timer.IdleTimer(3)
        self.receive_mode    = False
        self.mission_mode    = None
        self.response_list   = list()

    def connect(self):

        print("Connecting to {}:{}...".format(self.host, self.port))

        check = False
        while not check:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                check = agv_timer.alarm_timer(3, sock.connect, (self.host, self.port))  # Timeout
                if check:
                    print("Connect success !")
                    return sock
                else:
                    logger.warning("[Connect] Connection refused, socket reconnect !")  # Not socket error
            except socket.error as error:
                logger.warning("[Connect] Socket error: {}, socket reconnect !".format(error))
                time.sleep(1)

    def is_sock_error(self):

        while True:
            if self._sock_error:

                self.receive_mode = False
                ask_again = False
                if self.mission_mode is False:
                    self.mission_mode = None
                    ask_again = True
                self.reconnect()
                self.start_listen()
                if ask_again:
                    self.ask_mission()
                self._sock_error = False

    def reconnect(self):

        self.response_list = list()
        self.close()
        print("Reconnect after 3 second...")
        time.sleep(3)

        self._sock = self.connect()
        self.bind_request()

    def bind_request(self):

        print("Bind start !")
        new_pdu = agv_acmp.create_pdu("bind_request", self, device_id=agv_consts.MAC_ADDRESS)
        self.send_pdu(new_pdu)
        self.response_list.append({"resp_cmd_name": "bind_response", "seq": new_pdu.sequence_number})

        response = agv_timer.alarm_timer(5, self.receive_pdu)
        if response and not isinstance(response, bool):
            print(response.command_length, response.command_id, response.command_status, response.sequence_number)
            print("Bind success !")
        else:
            print("Bind fail, socket reconnect !")
            self.reconnect()

    def _mission_request(self):

        print("Mission request !")
        new_pdu = agv_acmp.create_pdu("mission_request", self, device_id=agv_consts.MAC_ADDRESS)
        self.send_pdu(new_pdu)
        self.response_list.append({"resp_cmd_name": "mission_response", "seq": new_pdu.sequence_number})

    def _mission_status_request(self, s, f, e):

        print("Mission status request !")
        new_pdu = agv_acmp.create_pdu("mission_status_request", self,
                                      device_id=agv_consts.MAC_ADDRESS, success=s, fail=f, error_msg=e)
        self.send_pdu(new_pdu)
        self.response_list.append({"resp_cmd_name": "mission_status_response", "seq": new_pdu.sequence_number})

    def _enquire_link_request(self):

        print("Enquire link request !")
        new_pdu = agv_acmp.create_pdu("enquire_link_request", self)
        self.send_pdu(new_pdu)
        self.response_list.append({"resp_cmd_name": "enquire_link_response", "seq": new_pdu.sequence_number})

    def send_pdu(self, pdu):

        logger.debug("Sending {} PDU".format(pdu.command_name))

        msg = pdu.generate_pdu()
        try:
            check = self._sock.sendall(msg)
            if check is not None:
                logger.warning("[Send] Send fail, socket reconnect !")
                self.reconnect()

        except socket.error as error:
            logger.warning("[Send] Socket error: {}, socket reconnect !".format(error))
            self.reconnect()

    def receive_pdu(self):

        logger.debug('Waiting for PDU...')

        try:
            raw_pdu_len = self._sock.recv(4)  # First check
            # time.sleep(0.1)
        except socket.error as error:
            logger.warning("[Receive] Socket error: {}, socket reconnect !".format(error))
            return None

        print(raw_pdu_len)

        if raw_pdu_len:
            try:
                length = struct.unpack('>I', raw_pdu_len)[0]
            except struct.error:
                logger.warning('[Receive] Receive broken pdu... {}'.format(repr(raw_pdu_len)))
                return None

            if length < agv_consts.HEADERS_LENGTH:
                logger.warning('[Receive] Receiving data were incomplete. {} < {}'
                               .format(length, agv_consts.HEADERS_LENGTH))
                return None

            raw_pdu = self._sock.recv(length - 4)
            raw_pdu = raw_pdu_len + raw_pdu

            get_pdu = agv_acmp.parse_pdu(raw_pdu, self)
            if get_pdu.is_status_error() or get_pdu.is_data_error(self.response_list):
                return None
            return get_pdu

        else:
            logger.warning("[Receive] Receive fail, socket reconnect !")
            return None

    def receive_thread(self):

        try:
            response = self.receive_pdu()
        except socket.error as error:
            logger.warning("[Receive_thread] Socket error: {}, socket reconnect !".format(error))
            return True

        if response is not None:
            print(response.command_length, response.command_id, response.command_status, response.sequence_number)
            if response.command_name == "enquire_link_response":
                print("Enquire link success !")
            elif response.command_name == "mission_response":
                if response.body is None:
                    print("There is no mission now...")
                    self._mission_request()
                    time.sleep(1)
                else:
                    self.mission_mode = True
                    is_mission_ongoing = self._mission_handler(response.body)
                    if is_mission_ongoing:
                        print("Mission is ongoing !")
                    else:
                        self.ask_mission()
            else:
                logger.warning('Unhandled command name {}'.format(response.command_name))
        else:
            logger.warning("[Receive_thread] Receive fail, socket reconnect !")
            return True

    def listen_receive_data(self):

        print("Receive mode turn on, start listen !")

        while self.receive_mode:

            error = self.receive_thread()
            if error:
                self.idle_timer.terminate()
                with self._sock_safe_lock:
                    self._sock_error  = True
                    break
            else:
                self.idle_timer.restart()  # timer restart

    def start_listen(self):

        self.receive_mode = True

        threading.Thread(target=self.listen_receive_data).start()
        threading.Thread(target=self.keep_socket_alive).start()

    def keep_socket_alive(self):

        current_sock = self._sock
        self.idle_timer.count_mode = False

        def check_resp():
            is_exist = False
            for item in self.response_list:
                if item["resp_cmd_name"] == "enquire_link_response":
                    is_exist = True
            return is_exist

        while self.receive_mode:
            if self.idle_timer.timeout :
                self._enquire_link_request()
                time.sleep(1)

                if current_sock == self._sock:
                    exist = check_resp()
                    if exist:
                        print("[Keep_socket_alive] Con't receive enquire link response, socket reconnect !")
                        self.idle_timer.terminate()
                        self._sock.shutdown(socket.SHUT_RDWR)  # socket send and receive are disallowed.
                        with self._sock_safe_lock:
                            self._sock_error = True
                            break
                    else:
                        self.idle_timer.restart()
            else:
                if self.idle_timer.count_mode is False:
                    self.idle_timer.start()

    def ask_mission(self):

        self.mission_mode = False
        self._mission_request()

    def _mission_handler(self, body):

        try:
            # mission_json_body = json.loads((body.decode("utf-8")))
            mission_json_body = body.decode("utf-8")

            if mission_json_body[-1] != "\0":
                logger.warning("[Mission_handler] Data received were incomplete.: {}".format(mission_json_body))
                return False
            else:
                mission_content = json.loads(mission_json_body[:-1])
        except (TypeError, ValueError):
            logger.warning("[Mission_handler] Data received were not in JSON format: {}".format(body))
            return False
        print(mission_content)
        if agv_mission.is_device_id_error(mission_content["device_id"]) or \
                agv_mission.is_field_name_error(mission_content) or agv_mission.is_value_not_string(mission_content):
            return False
        else:
            create_time = datetime.datetime.now().isoformat('T')
            submission_list = list()
            mission_db = agv_sqlite.SqliteModule(agv_sqlite.MIS_FILENAME, agv_sqlite.MIS_TABLE_NAME,
                                                 agv_sqlite.MIS_Headers)

            for submission_content in mission_content["mission"]:

                submission = agv_mission.submission_factory(submission_content["type"], submission_content)

                if submission is not None and submission.status is None:
                    mission_db.add_content(submission_content, "undone", create_time)
                    submission_list.append(submission)
                else:
                    mission_db.add_content(submission_content, submission.status, create_time)
                    return False

            threading.Thread(target=self._submission_thread, args=(submission_list, create_time,)).start()
            return True

    def _submission_thread(self, submission_list, create_time):

        def is_resp_have():
            is_exist = True
            while is_exist:
                for item in self.response_list:
                    if item["resp_cmd_name"] == "mission_status_response":
                        is_exist = False
            return False

        run_submission = None
        for run_submission in submission_list:
            print(run_submission.type)
            run_submission.do_submission()
            if run_submission.status != "Complete":
                break
            else:
                mission_db = agv_sqlite.SqliteModule(agv_sqlite.MIS_FILENAME, agv_sqlite.MIS_TABLE_NAME,
                                                     agv_sqlite.MIS_Headers)
                mission_db.update_content("status", run_submission.status, run_submission.id, create_time)

        while True:
            if self.receive_mode:
                self._mission_status_request(run_submission.success, run_submission.fail, run_submission.error_msg)
                if run_submission.status == "Complete" and not is_resp_have():
                    self.ask_mission()
                break

    def close(self):

        print('Socket close...')

        if self._sock:
            self._sock.close()
            self._sock = None
