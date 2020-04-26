import logging
from logging import Logger


def configure_logger(debug: bool = False) -> Logger:
    """
    This method configures the logging.  If the debug flag is set to true we
    turn on extra debugging logging.  Debug logging defaults to False
    """
    logger = logging.getLogger("PyPinyinTxt")
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    ch = ch = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
