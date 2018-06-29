import signal
import logging
import threading

logger = logging.getLogger("Exceptions")


class FunctionTimeout(Exception):
    """Function Timeout Error"""


def alarm_timer(timer, do_function, arg=None):

    def timeout_handler(signum, frame):
        raise FunctionTimeout

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timer)

    try:
        if arg is None:
            function_gain = do_function()
        else:
            function_gain = do_function(arg)

        if function_gain is None:
            function_gain = True

        return function_gain

    except FunctionTimeout:
        logger.warning("[{}] Timeout..., socket reconnect !".format(do_function))
        return False
    finally:
        signal.alarm(0)


class IdleTimer:

    def __init__(self, interval):
        self.interval = interval
        self.timer      = None
        self.timeout    = False
        self.count_mode = None

    def do_function(self):
        self.timeout = True

    def start(self):
        self.timer = threading.Timer(self.interval, self.do_function)
        self.timer.start()
        self.count_mode = True

    def restart(self):
        if self.timer:
            self.timer.cancel()
        self.count_mode = False
        self.timeout    = False

    def terminate(self):
        if self.timer:
            self.timer.cancel()
        self.timer      = None
        self.count_mode = None
        self.timeout    = False
