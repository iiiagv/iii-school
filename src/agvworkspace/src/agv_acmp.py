import agv_command


def create_pdu(command_name, client, **kwargs):

    new_pdu = agv_command.factory(command_name, client, **kwargs)

    return new_pdu


def parse_pdu(raw_pdu, client):

    command_name = agv_command.extract_command_id(raw_pdu)

    new_pdu = create_pdu(command_name, client)
    new_pdu.parse_pdu(raw_pdu)

    return new_pdu
