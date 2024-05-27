import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


def set_logger_level(level: int):
    logger.setLevel(level)


