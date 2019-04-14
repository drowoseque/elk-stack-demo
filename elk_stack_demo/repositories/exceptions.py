import logging
from logging import Logger
from typing import Dict, Any

import logstash

from elk_stack_demo import settings


def _get_logstash_handler() -> logstash.TCPLogstashHandler:
    return logstash.TCPLogstashHandler(**settings.LOGSTASH)


def _get_logger() -> Logger:
    logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)
    logger.addHandler(_get_logstash_handler())
    return logger


logger = _get_logger()


def log(exception, extra: Dict[str, Any]):
    logger.error(str(exception), extra=extra)
