import getpass
import logging

logger_service = logging.getLogger(__name__)
logger_service.setLevel(logging.INFO)


handler = logging.FileHandler(f"hub-service-log.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger_service.addHandler(handler)
logger_service.addHandler(logging.StreamHandler())


def log(msg: str):
    logger_service.info(msg)


def warn(msg: str):
    logger_service.warning(msg)


def err(msg: str):
    logger_service.error(msg)
