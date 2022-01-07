import pathlib
from logging import Logger, getLogger
from logging.config import fileConfig


def get_logger(workspace: str) -> Logger:
    logger = getLogger(workspace)
    directory = str(pathlib.Path(__file__).parent)
    fileConfig(f"{directory}/config/logging.conf", disable_existing_loggers=False)
    return logger
