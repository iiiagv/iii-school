import logging
import json
import struct

import agv_packet
import agv_consts


logger = logging.getLogger('Command')


def factory(command_name, client, **kwargs):

    try:
        return {
            "bind_request"           : BindRequest,
            "bind_response"          : BindResponse,
            "unbind_request"         : UnbindRequest,
            "unbind_response"        : UnbindResponse,
            "enquire_link_request"   : EnquireLinkRequest,
            "enquire_link_response"  : EnquireLinkResponse,
            "mission_request"        : MissionRequest,
            "mission_response"       : MissionResponse,
            "mission_status_request" : MissionStatusRequest,
            "mission_status_response": MissionStatusResponse,
        }[command_name](command_name, client, **kwargs)
    except KeyError:
        logger.warning('Command {} is not supported'.format(command_name))


def extract_command_id(raw_pdu):

    command_id = struct.unpack('>L', raw_pdu[4:8])[0]
    return SmppCommand.get_command_name(command_id)


class SmppCommand(agv_packet.SmppPDU):

    def __init__(self, command_name, client):

        super(SmppCommand, self).__init__(client)

        self.command_name    = command_name
        self.command_length  = agv_consts.HEADERS_LENGTH
        self.command_id      = self.get_command_id(command_name)
        self.command_status  = agv_consts.STATUS_ROK

    @staticmethod
    def _seq_num():

        if agv_consts.SEQ_COUNT_NUM < agv_consts.MAX_SEQUENCE:
            agv_consts.SEQ_COUNT_NUM += 1
        else:
            agv_consts.SEQ_COUNT_NUM = agv_consts.MIN_SEQUENCE
        return agv_consts.SEQ_COUNT_NUM

    @staticmethod
    def get_command_id(cmd_name):

        try:
            return agv_consts.COMMAND_ID_SET[cmd_name]
        except KeyError:
            logger.warning("Unknown command name '{}'".format(cmd_name))

    @staticmethod
    def get_command_name(cmd_id):

        try:
            for key, value in agv_consts.COMMAND_ID_SET.items():
                if value == cmd_id:
                    return key
        except KeyError:
            logger.warning("Unknown command code '0x{}'".format(cmd_id))

    @staticmethod
    def get_command_status_error_depiction(cmd_status):

        try:
            for key, value in agv_consts.COMMAND_STATUS_ERROR_CODE_SET.items():
                if value == cmd_status:
                    return key
        except KeyError:
            logger.warning("Unknown command code '0x{}'".format(cmd_status))


class BindRequest(SmppCommand):

    def __init__(self, command_name, client, **kwargs):
        super(BindRequest, self).__init__(command_name, client)

        self.body = (json.dumps(kwargs) + "\0").encode('utf-8')
        self.body_len = len(self.body)
        self.command_length += self.body_len
        self.sequence_number = self._seq_num()


class BindResponse(SmppCommand):

    def __init__(self, command_name, client):
        super(BindResponse, self).__init__(command_name, client)


class UnbindRequest(SmppCommand):

    def __init__(self, command_name, client):
        super(UnbindRequest, self).__init__(command_name, client)
        self.sequence_number = self._seq_num()


class UnbindResponse(SmppCommand):

    def __init__(self, command_name, client):
        super(UnbindResponse, self).__init__(command_name, client)


class EnquireLinkRequest(SmppCommand):

    def __init__(self, command_name, client):
        super(EnquireLinkRequest, self).__init__(command_name, client)
        self.sequence_number = self._seq_num()


class EnquireLinkResponse(SmppCommand):

    def __init__(self, command_name, client):
        super(EnquireLinkResponse, self).__init__(command_name, client)


class MissionRequest(SmppCommand):

    def __init__(self, command_name, client, **kwargs):
        super(MissionRequest, self).__init__(command_name, client)

        self.body = (json.dumps(kwargs) + "\0").encode('utf-8')
        self.body_len = len(self.body)
        self.command_length += self.body_len
        self.sequence_number = self._seq_num()


class MissionResponse(SmppCommand):

    def __init__(self, command_name, client):
        super(MissionResponse, self).__init__(command_name, client)


class MissionStatusRequest(SmppCommand):

    def __init__(self, command_name, client, **kwargs):
        super(MissionStatusRequest, self).__init__(command_name, client)

        self.body = (json.dumps(kwargs) + "\0").encode('utf-8')
        self.body_len = len(self.body)
        self.command_length += self.body_len
        self.sequence_number = self._seq_num()


class MissionStatusResponse(SmppCommand):

    def __init__(self, command_name, client):
        super(MissionStatusResponse, self).__init__(command_name, client)