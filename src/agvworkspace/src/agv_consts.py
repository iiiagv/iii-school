import subprocess

#
# Client Config
#
HEADERS_LENGTH      = 16
MAC_ADDRESS         = subprocess.getoutput('cat /var/lib/dbus/machine-id')

#
# Sequence Number
#
INITIAL_SEQUENCE = 0x00000000
MIN_SEQUENCE    = 0x00000001
MAX_SEQUENCE    = 0x7FFFFFFF
SEQ_COUNT_NUM   = INITIAL_SEQUENCE

#
# Command ID Set
#
COMMAND_ID_SET = {

    'bind_request'            : 0x00000001,
    'bind_response'           : 0x80000001,
    'enquire_link_request'    : 0x00000015,
    'enquire_link_response'   : 0x80000015,
    'unbind_request'          : 0x00000006,
    'unbind_response'         : 0x80000006,
    'mission_request'         : 0x00000030,
    'mission_response'        : 0x80000030,
    'mission_status_request'  : 0x00000031,
    'mission_status_response' : 0x80000031,
    'robot_status_request'    : 0x00000032,
    'robot_status_response'   : 0x80000032,

}


#
# Command Status Error Code
#
STATUS_ROK = 0x00000000 # No Error

COMMAND_STATUS_ERROR_CODE_SET = {

    'STATUS_RINVMSGLEN'     : 0x00000001,  # Message Length is invalid
    'STATUS_RINVCMDLEN'     : 0x00000002,  # Command Length is invalid
    'STATUS_RINVCMDID'      : 0x00000003,  # Invalid Command ID
    'STATUS_RSYSERR'        : 0x00000008,  # System Error
    'STATUS_RBINDFAIL'      : 0x00000010,  # Bind Failed
    'STATUS_RINVBODY'       : 0x00000040,  # Invalid Packet Body Data
    'STATUS_RINVJSON'       : 0x00000042,  # Invalid JSON Data

}


