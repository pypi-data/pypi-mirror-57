# -*- coding:utf-8 -*-
#################
# Logging
#################
import os
import time
import logging
# from logging.handlers import TimedRotatingFileHandler


def strftime(t=None):
    return time.strftime("%Y%m%d-%H%M%S", time.localtime(t or time.time()))


logging.basicConfig(
    format="[ %(asctime)s][%(module)s.%(funcName)s] %(message)s")
DEFAULT_LEVEL = logging.INFO
DEFAULT_LOGGING_DIR = None
fh = None


def init_fh():
    """Initialize the global file_handler for LOGGER."""
    global fh
    if fh is not None:
        return
    if DEFAULT_LOGGING_DIR is None:
        return
    if not os.path.exists(DEFAULT_LOGGING_DIR):
        os.makedirs(DEFAULT_LOGGING_DIR)
    logging_path = os.path.join(DEFAULT_LOGGING_DIR, strftime() + ".log")
    fh = logging.FileHandler(logging_path)
    fh.setFormatter(logging.Formatter(
                    "[ %(asctime)s][%(module)s.%(funcName)s] %(message)s"))


def update_default_level(default_level):
    """Update the logging level for logger.

    Parameters
    ----------
    default_level: const int
        A value in the set {logging.DEBUG, logging.INFO, logging.WARNING, 
        logging.ERROR, logging.CRITICAL}
    """
    global DEFAULT_LEVEL
    DEFAULT_LEVEL = default_level


def update_default_logging_dir(default_logging_dir):
    """Update the dir to place the logging file.

    Parameters
    ----------
    default_logging_dir: string
    """
    global DEFAULT_LOGGING_DIR
    DEFAULT_LOGGING_DIR = default_logging_dir


def get_logger(name="safeu", level=None):
    """Fetch the logger with name and level.

    Parameters
    ----------
    name: string, optional (default="safeu")

    level: const int, optional(default=None)
        A value in the set {logging.DEBUG, logging.INFO, logging.WARNING, 
        logging.ERROR, logging.CRITICAL} If None, the returned logger will 
        have the default logging level set by `update_default_level`.
    
    Return
    ------
    logger: A logger object
        Call logger.[debug/info/warning/error/critical](msg, *arg, **kwargs) to 
        add logging. Refer to https://docs.python.org/3/howto/logging.html.
    """
    level = level or DEFAULT_LEVEL
    logger = logging.getLogger(name)
    logger.setLevel(level)
    init_fh()
    if fh is not None:
        logger.addHandler(fh)
    return logger
