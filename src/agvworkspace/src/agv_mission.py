import logging
import ast
import os
import rospy
import threading

import ipc_gpio_cl
import agv_consts
from agvcode.srv import AgvNav

BODY_FIELD    = {"device_id", "mission"}
MISSION_FIELD = {"id", "type", "parameter"}

logger = logging.getLogger('mission')


def is_device_id_error(device_id):

    if device_id == agv_consts.MAC_ADDRESS:
        return False
    else:
        logger.warning("Device_id is {}, not {} !".format(agv_consts.MAC_ADDRESS, device_id))
        return True


def is_field_name_error(content):

    is_error = False

    if set(content.keys()) == BODY_FIELD:

        m_all_field = [set(field.keys()) for field in content["mission"]]
        for m_field in m_all_field:
            if m_field != MISSION_FIELD:
                is_error = True
                logger.warning("Mission's field are error: {}".format(m_all_field))
                break
        return is_error

    else:
        is_error = True
        logger.warning("Body's field are error: {}".format(content.keys()))
        return is_error


def is_value_not_string(content):

    is_error = False

    m_all_values = [list(field.values()) for field in content["mission"]]
    for m_values in m_all_values:
        # print(m_values)
        if not all(isinstance(value, str) for value in m_values):
            is_error = True
            # for i in m_values:
            #     print(i, type(i))
            logger.warning("Mission's value isn't string: {}".format(m_values))
            break
    return is_error


def submission_factory(submis_type, submis_content):

    try:
        return {

            "SET" : SetParamMission,
            "MAP" : SlamMission,
            "NAV" : NavigationMission,
            "LOC" : SceneLocationMission,
            "MDR" : MandrelMission,
            "CHAG": ChargingMission

        }[submis_type](submis_content)
    except KeyError:
        logger.warning('Mission type {} is not supported'.format(submis_type))
        return None


class SubMissionObject:

    def __init__(self, content):

        self.id        = content["id"]
        self.type      = content["type"]
        self.parameter = None
        self.status    = None
        self.cmd       = None

        self.success   = None
        self.fail      = None
        self.error_msg = None

    def start_submission(self, cmd):
        exec(cmd)

    def do_submission(self):

        if self.type == "NAV":

            threading.Thread(target=self.start_submission, args=(self.cmd,)).start()

            # rospy.init_node('submission_client')
            rospy.wait_for_service('agv_nav')
            go_forward = rospy.ServiceProxy('agv_nav', AgvNav)
            response = go_forward(self.parameter)

            if response.status:
                self.status    = "Complete"
                self.success   = "true"
                self.fail      = "false"
                self.error_msg = response.error_msg
            else:
                self.status    = "Fail"
                self.success   = "false"
                self.fail      = self.type
                self.error_msg = response.error_msg

            os.system("rosnode kill /agvontheway_serv")

        if self.type == "MDR":

            gpio_start = ipc_gpio_cl.IPC_gpio()
            gpio_start.gpio_set_pin_direction(2, ipc_gpio_cl.EAPI_GPIO_OUTPUT)
            exec(self.cmd)
            gpio_start.gpio_uninitialize()

            self.status    = "Complete"
            self.success   = "true"
            self.fail      = "false"
            self.error_msg = "none"


class SetParamMission(SubMissionObject):

    def __init__(self, content):
        super(SetParamMission, self).__init__(content)

        try:
            param = ast.literal_eval(content["parameter"])

            if isinstance(param, dict):
                self.parameter = param
                self.cmd = "os.system('rosrun agvcode set_param.py')"

            else:
                self.status = "Parameter's type is {}, not {} !".format("dict", type(param))

        except (ValueError, SyntaxError):
            self.status = "Parameter's type is {}, not {} !".format("dict", type(content["parameter"]))


class SlamMission(SubMissionObject):

    def __init__(self, content):
        super(SlamMission, self).__init__(content)

        if not content["parameter"]:
            self.cmd = "os.system('rosrun agvcode slam.py')"

        else:
            self.status = "Don't give SlamMission parameter: {} !".format(content["parameter"])


class NavigationMission(SubMissionObject):

    def __init__(self, content):
        super(NavigationMission, self).__init__(content)

        try:
            param = ast.literal_eval(content["parameter"])

            if isinstance(param, list):
                self.parameter = str(param)
                self.cmd = "os.system('rosrun agvcode agv_navigation.py')"

            else:
                self.status = "Parameter's type is {}, not {} !".format("list", type(param))

        except (ValueError, SyntaxError):
            self.status = "Parameter's type is {}, not {} !".format("list", type(content["parameter"]))


class SceneLocationMission(SubMissionObject):

    def __init__(self, content):
        super(SceneLocationMission, self).__init__(content)

        if not content["parameter"]:
            self.cmd = "os.system('rosrun agvcode slam.py')"

        else:
            self.status = "Don't give SceneLocationMission parameter: {} !".format(content["parameter"])


class MandrelMission(SubMissionObject):

    def __init__(self, content):
        super(MandrelMission, self).__init__(content)

        if content["parameter"] == "up":
            self.parameter = content["parameter"]
            self.cmd = "gpio_start.gpio_set_pin_level(2, ipc_gpio_cl.EAPI_GPIO_VOL_HIGH)"

        elif content["parameter"] == "down":

            self.parameter = content["parameter"]
            self.cmd = "gpio_start.gpio_set_pin_level(2, ipc_gpio_cl.EAPI_GPIO_VOL_LOW)"

        else:
            self.status = "Parameter is up or down, not {} !".format(content["parameter"])


class ChargingMission(SubMissionObject):

    def __init__(self, content):
        super(ChargingMission, self).__init__(content)

        try:
            param = ast.literal_eval(content["parameter"])

            if isinstance(param, int):
                self.parameter = param
                self.cmd = "os.system('rosrun agvcode charging.py')"

            else:
                self.status = "Parameter's type is {}, not {} !".format("int", type(param))

        except (ValueError, SyntaxError):
            self.status = "Parameter's type is {}, not {} !".format("int", type(content["parameter"]))