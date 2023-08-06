import traceback
import logging

try:
    from accpac import (showMessageBox,
                        program, rotoID,
                        error, message, warning, )
except ImportError as e:
    # This happens when the tools are imported outside of the Extender env.
    # We can pass to let the tool do its work (likely sphinx making docs).
    pass

class ExMessages(object):
    """A logger like object for writing messages for the user.

    The ExtenderMessageWriter acts like a logger, allowing a developer
    to add messages that are only displayed to the user if the current
    level is greater than or equal to the message level being called.

    Messages at debug and below, as well as those at error or above,
    support displaying the last exception traceback to make debugging
    easier.

    :param name: the name to log under.
    :type name: str
    :param level: the level at and below which to display messages.
    :type level: int
    :param log_path: the path of a log file to write to.
    :type log_path: str
    :param programs: the list of programs for which to display
        messages.  For example, if programs were ["OE1100", ] then messages
        will only be displayed if the Order Entry program is currently
        running.
    :type programs: list
    :param box: indicates whether to show a message box or
        add a message to the Sage message stack. Defaults to True.
    :type box: list
    :param disabled: disable all messages and logging.
        Defaults to False.
    :type disabled: bool
    """

    """Supported Levels"""
    PANIC       = 0
    CRITICAL    = 1
    ERROR       = 5
    WARNING     = 10
    INFO        = 15
    DEBUG       = 20
    RAW         = 25

    LEVELS = (
            PANIC,
            CRITICAL,
            ERROR,
            WARNING,
            INFO,
            DEBUG,
            RAW,
            )
    """Supported log levels in decreasing order of severity."""

    # Level names and log method lookup
    _LEVEL_INFO= {
            PANIC: ("Panic", "critical", ),
            CRITICAL: ("Critical", "critical", ),
            ERROR: ("Error", "error", ),
            WARNING: ("Warning", "warning", ),
            INFO: ("Info", "info", ),
            DEBUG: ("Debug", "debug", ),
            RAW: ("Raw", "debug", ),
            }

    def __init__(self, name, level=None, log_path=None, programs=[], box=True,
                 disabled=False, ):
        """Get a new ExMessages instance."""
        if not level:
            level = self.INFO
        self.level = level
        self.level_info = self._LEVEL_INFO[level]
        self.level_name = self.level_info[0]

        self.name = name
        self.disabled = disabled
        self.programs = programs
        self.box = box

        self.log = None
        self.log_path = log_path
        self.log_level = getattr(logging, self.level_info[1])
        if self.log_path:
            self._setup_log()

    def _setup_log(self):
        self.log = logging.getLogger(name)
        self.log.setLevel(self.log_level.DEBUG)
        self.log_formatter = logging.Formatter(
                '%(asctime)s - %(name)s %(message)s')
        self.log_handler = logging.FileHandler(self.log_path)
        self.log_handler.setFormatter(self.log_formatter)
        self.log.addHandler(self.log_handler)

    def _write(self, level, msg):
        if self.disabled or (self.programs and program not in self.programs):
            return None

        msg_w_name = "{}\n\n{}".format(self.name, msg)
        if level <= self.level:
            if self.box:
                showMessageBox(msg_w_name)
            else:
                if level <= self.ERROR:
                    error(msg_w_name)
                elif level <= self.WARNING:
                    warning(msg_w_name)
                else:
                    message(msg_w_name)

        if self.log:
            log_func = getattr(self.log, self._LEVEL_INFO[self.level][1])
            log_func(msg)

        return msg

    def panic(self, msg, exc_info=None):
        """Display and log a panic message.

        :param msg: message to write.
        :type msg: str
        :param exc_info: include last exception backtrace?
        :type exc_info: bool

        :rtype: None
        """
        if exc_info:
            msg = "\n".join([msg, traceback.format_exc(), ])
        self._write(self.PANIC, msg)

    def crit(self, msg, exc_info=None):
        """Display and log a critical message.

        :param msg: message to write.
        :type msg: str
        :param exc_info: include last exception backtrace?
        :type exc_info: bool
        :rtype: None
        """
        if exc_info:
            msg = "\n".join([msg, traceback.format_exc(), ])
        self._write(self.CRITICAL, msg)

    def error(self, msg, exc_info=None):
        """Display and log an error message.

        :param msg: message to write.
        :type msg: str
        :param exc_info: include last exception backtrace?
        :type exc_info: bool
        :rtype: None
        """
        if exc_info:
            msg = "\n".join([msg, traceback.format_exc(), ])
        self._write(self.ERROR, msg)

    def warn(self, msg):
        """Display and log a warning message.

        :param msg: message to write.
        :type msg: str
        :rtype: None
        """
        self._write(self.WARNING, msg)

    def info(self, msg):
        """Display and log an info message.

        :param msg: message to write.
        :type msg: str
        :rtype: None
        """
        self._write(self.INFO, msg)

    def debug(self, msg, exc_info=False):
        """Display and log a debug message.

        :param msg: message to write.
        :type msg: str
        :param exc_info: include last exception backtrace?
        :type exc_info: bool
        :rtype: None
        """
        msg = "DEBUG {}\n---------\n{}".format(rotoID, msg)
        if exc_info:
            msg = "\n".join([msg, traceback.format_exc(), ])
        self._write(self.DEBUG, msg)

    def raw(self, msg, exc_info=False):
        """Display and log raw output.

        :param msg: message to write.
        :type msg: str
        :param exc_info: include last exception backtrace?
        :type exc_info: bool
        :rtype: None
        """
        msg = "RAW {}\n---------\n{}".format(rotoID, msg)
        if exc_info:
            msg = "\n".join([msg, traceback.format_exc(), ])
        self._write(self.RAW, msg)
