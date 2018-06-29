import ctypes

_path = '/usr/local/SEMA/lib/libsemaeapi.so'
_mod = ctypes.cdll.LoadLibrary(_path)

# define
EAPI_STATUS_SUCCESS = 0

EAPI_GPIO_ADC = 4
EAPI_GPIO_1WIRE = 2
EAPI_GPIO_INPUT = 1
EAPI_GPIO_OUTPUT = 0

EAPI_GPIO_VOL_HIGH = 1
EAPI_GPIO_VOL_LOW = 0

IP_VERTION = ctypes.c_char
IP_V4 = IP_VERTION(0)
IP_V6 = IP_VERTION(1)

GPIO_NUM = 9
GPIO_ALL_PINS = range(0, GPIO_NUM+1)

def EAPI_GPIO_GPIO_ID(pin):
    if 0 <= pin <= GPIO_NUM:
        return pin
    else:
        raise ValueError('GPIO pin out of range (values 0 ~ 9)')

# LibInitialize
# SemaEApiLibInitialize(false, IP_V4, ipAddr, 0, (char*)"123", &handler)
SemaEInitialize = _mod.SemaEApiLibInitialize
SemaEInitialize.argtypes = (ctypes.c_bool, ctypes.c_char, ctypes.POINTER(ctypes.c_char),
                            ctypes.c_uint32, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_uint32))
SemaEInitialize.restype = ctypes.c_uint32

# LibUninitialise
# SemaEApiLibUnInitialize(handler)
SemaEUnInitialize = _mod.SemaEApiLibUnInitialize
SemaEUnInitialize.argtypes = (ctypes.c_uint32, )
SemaEUnInitialize.restype = ctypes.c_uint32

# GPIOGetDirectionCaps
# SemaEGPIOGetDirectionCaps(handler, EAPI_GPIO_GPIO_ID(pin), ctypes.pointer(buffer1), ctypes.pointer(buffer2))
SemaEGPIOGetDirectionCaps = _mod.SemaEApiGPIOGetDirectionCaps
SemaEGPIOGetDirectionCaps.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32))
SemaEGPIOGetDirectionCaps.restype = ctypes.c_uint32

# GPIOGetDirection
# SemaEApiGPIOGetDirection(handler,EAPI_GPIO_GPIO_ID(pin),0x01,&directionCheck)
SemaEGPIOGetDirection = _mod.SemaEApiGPIOGetDirection
SemaEGPIOGetDirection.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
SemaEGPIOGetDirection.restype = ctypes.c_uint32

# GPIOSetDirection
# SemaEApiGPIOSetDirection(handler,EAPI_GPIO_GPIO_ID(pin),0x01,direction)
SemaEGPIOSetDirection = _mod.SemaEApiGPIOSetDirection
SemaEGPIOSetDirection.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
SemaEGPIOSetDirection.restype = ctypes.c_uint32


# GPIOSetLevel
# SemaEApiGPIOSetLevel(handler,EAPI_GPIO_GPIO_ID(pin),0x01,level)
SemaEGPIOSetLevel = _mod.SemaEApiGPIOSetLevel
SemaEGPIOSetLevel.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32)
SemaEGPIOSetLevel.restype = ctypes.c_uint32

# GPIOGetLevel
# SemaEApiGPIOGetLevel(handler,EAPI_GPIO_GPIO_ID(pin),0x01,&buffer)
SemaEGPIOGetLevel = _mod.SemaEApiGPIOGetLevel
SemaEGPIOGetLevel.argtypes = (ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(ctypes.c_uint32))
SemaEGPIOGetLevel.restype = ctypes.c_uint32

# GPIOPinGetConfig
SemaEGPIOPinGetConfig = _mod.SemaEApiGPIOPinGetConfig
SemaEGPIOPinGetConfig.argtypes = (ctypes.c_uint32, ctypes.c_uint8, ctypes.POINTER(ctypes.c_uint32))
SemaEGPIOPinGetConfig.restype = ctypes.c_uint32

# GPIOPinGetConfig
SemaEGPIOPinSetConfig = _mod.SemaEApiGPIOPinSetConfig
SemaEGPIOPinSetConfig.argtypes = (ctypes.c_uint32, ctypes.c_uint8, ctypes.c_uint32)
SemaEGPIOPinSetConfig.restype = ctypes.c_uint32

# GPIOPinGetCap
SemaEGPIOPinGetCap = _mod.SemaEApiGPIOPinGetCap
SemaEGPIOPinGetCap.argtypes = (ctypes.c_uint32, ctypes.c_uint8, ctypes.POINTER(ctypes.c_uint32))
SemaEGPIOPinGetCap.restype = ctypes.c_uint32

# GPIOPinGetADCValue
SemaEGPIOPinGetADCValue = _mod.SemaEApiGPIOPinGetADCValue
SemaEGPIOPinGetADCValue.argtypes = (ctypes.c_uint32, ctypes.c_uint8, ctypes.POINTER(ctypes.c_uint32))
SemaEGPIOPinGetADCValue.restype = ctypes.c_uint32

# Initialize GPIO parameter
GPIO_INIT_HANDLER = ctypes.c_uint32(0)
GPIO_IPADDR = '127.0.0.1'
GPIO_PORT = 0
GPIO_PWD = '123'

class IPC_gpio():

    def __init__(self):
        self.handler = self.gpio_initialize(0, 0, GPIO_IPADDR, GPIO_PORT, GPIO_PWD, GPIO_INIT_HANDLER)

    # Initialize API
    def gpio_initialize(self, ssl, ipv, pHostip, port, pPasswd, handler):
        # GPIO_CL.SemaEInitialize(False, ipvertion(0), ipAddr, port, pwd, ctypes.pointer(handler))
        sslbool = (False, True)
        ipAddr = ctypes.c_char_p(bytes(pHostip.encode()))
        pwd = ctypes.c_char_p(bytes(pPasswd.encode()))
        ret = ctypes.c_uint32(0)
        ret = SemaEInitialize(sslbool[ssl], IP_VERTION(ipv), ipAddr, port, pwd, ctypes.pointer(handler))
        if (ret != EAPI_STATUS_SUCCESS):
            print("Can't initialize SEMA Lib. Error code: " + str(ret) + "\n\n")
        else:
            print("SEMA Lib is initial\n\n")
        return handler

    # Close API
    def gpio_uninitialize(self):
        SemaEUnInitialize(self.handler)
        print("SEMA Lib is uninitial\n\n")

    # TODO: For Set

    # 設定各Pin腳之狀態(輸入或輸出)
    # gpio_set_need_pin_direction([1, 3, 5], EAPI_GPIO_OUTPUT)
    def gpio_set_need_pin_direction(self, pins, direction):
        directionCheck = ctypes.c_uint32(0)
        ret = ctypes.c_uint32(0)
        bitmask = 0
        for num in pins:
            if num <= GPIO_NUM:
                bitmask = bitmask + 2 ** num
            else:
                raise ValueError('GPIO pin out of range (values 0 ~ 9)')

        ret = SemaEGPIOSetDirection(self.handler, EAPI_GPIO_GPIO_ID(0), bitmask, direction)
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error setting GPIO direction: 0x" + str(ret) + "\n\n")
        self.gpio_get_all_pin_direction()

    # 設定各PIN腳之電位
    # gpio_set_need_pin_level([1, 3, 5], EAPI_GPIO_VOL_HIGH)
    def gpio_set_need_pin_level(self, pins, level):
        ret = ctypes.c_uint32(0)
        bitmask = 0
        for num in pins:
            if num <= GPIO_NUM:
                bitmask = bitmask + 2 ** num
            else:
                raise ValueError('GPIO pin out of range (values 0 ~ 9)')
        ret = SemaEGPIOSetDirection(self.handler, EAPI_GPIO_GPIO_ID(0), bitmask, EAPI_GPIO_OUTPUT)
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error setting GPIO direction: 0x" + str(ret) + "\n\n")
        ret = SemaEGPIOSetLevel(self.handler, EAPI_GPIO_GPIO_ID(0), bitmask, level)
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error setting GPIO level: 0x" + str(ret) + "\n\n")
        pinnum = 0
        buffer = ctypes.c_uint32(0)
        # while pinnum <= GPIO_NUM:
        for pinnum in pins:
            ret = SemaEGPIOGetLevel(self.handler, EAPI_GPIO_GPIO_ID(pinnum), 0x01, ctypes.pointer(buffer))
            if (ret != EAPI_STATUS_SUCCESS):
                print("Error getting GPIO level: 0x" + str(ret) + "\n\n")
            else:
                print("Reading GPIO pin " + str(pinnum) + " input level: " + str(buffer.value) + "\n")
                if pinnum == GPIO_NUM:
                    print("\n")
                # pinnum = pinnum + 1

    # 2.10.3
    # 設定Pin腳為輸出或輸入
    # Sets the specified GPIO pin to be an input or an output
    # handler   : the board handle
    # pin       : the GPIO pin number (values 0 ~ 15)
    # direction : EAPI_GPIO_INPUT for input
    #             EAPI_GPIO_OUTPUT for output
    def gpio_set_pin_direction(self, pin, direction):
        directionCheck = ctypes.c_uint32(0)
        ret = ctypes.c_uint32(0)
        print("Setting pin " + str(pin) + " direction\n")

        # SemaEApiGPIOSetDirection(handler,EAPI_GPIO_GPIO_ID(pin),0x01,direction)
        ret = SemaEGPIOSetDirection(self.handler, EAPI_GPIO_GPIO_ID(pin), 0x01, direction)

        if (ret != EAPI_STATUS_SUCCESS):
            print("Error setting GPIO direction: 0x" + str(ret) + "\n\n")

        # SemaEApiGPIOGetDirection(handler, EAPI_GPIO_GPIO_ID(pin), 0x01, & directionCheck)
        ret = SemaEGPIOGetDirection(self.handler, EAPI_GPIO_GPIO_ID(pin), 0x01, ctypes.pointer(directionCheck))
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error checking GPIO direction: 0x" + str(ret) + "\n\n")
        else:
            print("Direction: " + str(directionCheck.value) + " (1 = input, 0 = output)\n\n")

    # 2.10.5
    # 設定PIN腳的電位
    # Sets the specified GPIO pin level to be HIGH (3.3V) or LOW (0V).
    # Only affects GPIO pins configured as outputs
    # handler   : the board handle
    # pin       : the GPIO pin number (values 0 ~ 15)
    # direction : EAPI_GPIO_HIGH for high
    #             EAPI_GPIO_LOW for low
    def gpio_set_pin_level(self, pin, level):
        # buffer = ctypes.c_uint32(0)
        ret = ctypes.c_uint32(0)
        print("Setting pin " + str(pin) + " output level to " + str(level) + "\n\n")
        # SemaEApiGPIOSetLevel(handler,EAPI_GPIO_GPIO_ID(pin),0x01,level)
        ret = SemaEGPIOSetLevel(self.handler, EAPI_GPIO_GPIO_ID(pin), 0x01, level)
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error setting GPIO level: 0x" + str(ret) + "\n\n")

    # 2.10.7
    # 設定當下PIN腳的屬性(OUTPUT(0), INPUT(1), 1-WIRE(2), ADC(4))
    #                 (EAPI_GPIO_OUTPUT, EAPI_GPIO_INPUT, EAPI_GPIO_1WIRE, EAPI_GPIO_ADC)
    # Read the configuration value of GPIO pins for the selected GPIO capabilities.
    def gpio_pin_set_config(self, pin, config):
        ret = ctypes.c_uint32(0)
        ret = SemaEGPIOPinSetConfig(self.handler, EAPI_GPIO_GPIO_ID(pin), config)
        if (ret != EAPI_STATUS_SUCCESS):
            raise IOError('GPIO pin ' + str(pin) + ' can\'t set this config')
        for pinnum in GPIO_ALL_PINS:
            self.gpio_pin_get_config(pinnum)

    # TODO: For Read

    # 2.10.4
    # 取得PIN腳的電位
    # Reads the specified GPIO pin level and prints it. For use with pins configured as inputs.
    # handler   : the board handle
    # pin       : the GPIO pin number (values 0 ~ 15)
    def gpio_read_pin_level(self, pin):
        buffer = ctypes.c_uint32(0)
        ret = ctypes.c_uint32(0)
        # SemaEApiGPIOGetLevel(handler,EAPI_GPIO_GPIO_ID(pin),0x01,&buffer)
        ret = SemaEGPIOGetLevel(self.handler, EAPI_GPIO_GPIO_ID(pin), 0x01, ctypes.pointer(buffer))
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error getting GPIO level: 0x" + str(ret) + "\n\n")
        else:
            print("Reading GPIO pin " + str(pin) + " input level: " + str(buffer.value) + "\n\n")

    # 2.10.8
    # 取得當下PIN腳的屬性(OUTPUT, INPUT, 1-WIRE, ADC)
    # Read the configuration value of GPIO pins for the selected GPIO capabilities.
    def gpio_pin_get_config(self, pin):
        ret = ctypes.c_uint32(0)
        buffer = ctypes.c_uint32(0)
        ret = SemaEGPIOPinGetConfig(self.handler, EAPI_GPIO_GPIO_ID(pin), ctypes.pointer(buffer))
        if buffer.value == 0:
            print("Pin " + str(pin) + " Config: " + "GPIO_OUTPUT\n\n")
        elif buffer.value == 1:
            print("Pin " + str(pin) + " Config: " + "GPIO_INPUT\n\n")
        elif buffer.value == 2:
            print("Pin " + str(pin) + " Config: " + "GPIO_1-WIRE\n\n")
        elif buffer.value == 4:
            print("Pin " + str(pin) + " Config: " + "GPIO_A/D converter (ADC)\n\n")

    # 取得所有Pin腳的狀態(輸入或輸出)
    # Get all of Pin's direction(input or output)
    def gpio_get_all_pin_direction(self):
        directionCheck = ctypes.c_uint32(0)
        ret = ctypes.c_uint32(0)
        pinnum = 0
        while pinnum <= GPIO_NUM:
            ret = SemaEGPIOGetDirection(self.handler, EAPI_GPIO_GPIO_ID(pinnum), 0x01, ctypes.pointer(directionCheck))
            if (ret != EAPI_STATUS_SUCCESS):
                print("Error checking GPIO direction: 0x" + str(ret) + "\n\n")
            else:
                print("Pin " + str(pinnum) + " Direction: " + str(directionCheck.value) + " (1 = input, 0 = output)\n")
                if pinnum == GPIO_NUM:
                    print("\n")
                pinnum = pinnum + 1

    # TODO: Not Use

    # 2.10.1
    # 確認PIN腳是否具備GPIO功能
    # Reads the capabilities of the current GPIO implementation from the selected GPIO interface.
    # The ports where both input and output bit masks are 1 are GPIOs.
    # handler   : the board handle
    # pin       : the GPIO pin number (values 0 ~ 15)
    def gpio_get_direction_caps(self, pin):
        buffer1 = ctypes.c_uint32(0)
        buffer2 = ctypes.c_uint32(0)
        ret = ctypes.c_uint32(0)
        ret = SemaEGPIOGetDirectionCaps(self.handler, EAPI_GPIO_GPIO_ID(pin), ctypes.pointer(buffer1),
                                        ctypes.pointer(buffer2))
        if (ret != EAPI_STATUS_SUCCESS):
            print("Error getting GPIO level: 0x" + str(ret) + "\n\n")
        else:
            print('InputBitMask:' + str(buffer1.value) + "\n")
            print('OutputBitMask:' + str(buffer2.value) + "\n")
            if buffer1.value == 1 & buffer2.value == 1:
                print("Pin " + str(pin) + " is GPIO\n\n")

    # 2.10.6
    # 取得PIN腳具備的所有功能(GPIO, 1-WIRE, ADC)
    # Reads the capabilities value of GPIO pins.
    def gpio_pin_get_cap(self, pin):
        ret = ctypes.c_uint32(0)
        buffer = ctypes.c_uint32(0)
        ret = SemaEGPIOPinGetCap(self.handler, EAPI_GPIO_GPIO_ID(pin), ctypes.pointer(buffer))
        if buffer.value == 0:
            print("Pin " + str(pin) + " Capabilities: " + "not available\n\n")
        elif buffer.value == 1:
            print("Pin " + str(pin) + " Capabilities: " + "GPIO\n\n")
        elif buffer.value == 2:
            print("Pin " + str(pin) + " Capabilities: " + "1-WIRE\n\n")
        elif buffer.value == 3:
            print("Pin " + str(pin) + " Capabilities: " + "GPIO, 1-WIRE\n\n")
        elif buffer.value == 4:
            print("Pin " + str(pin) + " Capabilities: " + "A/D converter (ADC)\n\n")
        elif buffer.value == 5:
            print("Pin " + str(pin) + " Capabilities: " + "GPIO, A/D converter (ADC)\n\n")
        elif buffer.value == 6:
            print("Pin " + str(pin) + " Capabilities: " + "1-WIRE, A/D converter (ADC)\n\n")
        elif buffer.value == 7:
            print("Pin " + str(pin) + " Capabilities: " + "GPIO, 1-WIRE, A/D converter (ADC)\n\n")

    # 取得PIN腳的ADC電壓值
    def gpio_pin_get_ADC_value(self, pin):
        ret = ctypes.c_uint32(0)
        buffer1 = ctypes.c_uint32(0)
        buffer2 = ctypes.c_uint32(0)
        ret = SemaEGPIOPinGetConfig(self.handler, EAPI_GPIO_GPIO_ID(pin), ctypes.pointer(buffer1))
        if buffer1.value == 4:
            ret = SemaEGPIOPinGetADCValue(self.handler, EAPI_GPIO_GPIO_ID(pin), ctypes.pointer(buffer2))

            print("Pin " + str(pin) + " ADC value: " + str(buffer2.value) + "\n")
            print("Pin " + str(pin) + " ADC value: " + str(round(buffer2.value / 1023 * 3.3, 3)) + "V\n\n")
            # print("Pin " + str(pin) + " ADC value: " + str(buffer2.value/1023*3.3) + "\n")
        else:
            print('GPIO pin ' + str(pin) + '\'s configuration isn\'t A/D converter')
