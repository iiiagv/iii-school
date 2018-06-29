import struct
import json
import logging

import agv_consts

logger = logging.getLogger('PDU')


class SmppPDU(object):

    def __init__(self, client):

        # initial PDU config
        self._client      = client
        self.command_name = None
        self.body_len     = 0

        # initial PDU headers + body
        self.command_length  = None
        self.command_id      = None
        self.command_status  = None
        self.sequence_number = None
        self.body            = None

    def is_status_error(self):

        error = False
        if self.command_status != agv_consts.STATUS_ROK:
            from agv_command import SmppCommand
            cmd_error_code_depiction = SmppCommand.get_command_status_error_depiction(self.command_status)
            logger.warning('Error code depiction: {}'.format(cmd_error_code_depiction))
            error = True
        return error

    def is_data_error(self, check_list):

        error = False
        data_dick = {"resp_cmd_name": self.command_name, "seq": self.sequence_number}
        # print(check_list)
        if data_dick not in check_list:
            logger.warning("Error cmd_id: {}, seq: {}".format(hex(self.command_id), self.sequence_number))
            error = True
        else:
            check_list.remove(data_dick)
        return error

    def generate_pdu(self):

        if self.body:
            message = struct.pack(">4I{}s".format(self.body_len), self.command_length, self.command_id,
                                  self.command_status, self.sequence_number, self.body)
        else:
            message = struct.pack(">4I".format(self.body_len), self.command_length, self.command_id,
                                  self.command_status, self.sequence_number)
        return message

    def parse_pdu(self, raw_pdu):

        headers = raw_pdu[0:agv_consts.HEADERS_LENGTH]
        chunks  = struct.unpack('>4I', headers)
        self.command_length  = chunks[0]
        self.command_id      = chunks[1]
        self.command_status  = chunks[2]
        self.sequence_number = chunks[3]

        if len(raw_pdu) > agv_consts.HEADERS_LENGTH:
            self.body_len = self.command_length - agv_consts.HEADERS_LENGTH
            self.body     = raw_pdu[agv_consts.HEADERS_LENGTH:]
            # self.body     = json.loads((self.body.decode("utf-8"))[:-1])
