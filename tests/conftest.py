import sys
import pytest
from loguru import logger


def pytest_addoption(parser):
    """Adds options to pytest"""
    parser.addoption(
        "--loguru-level",
        action="store",
        default="INFO",
        help="Loguru logging level (TRACE, DEBUG,"
             " INFO, WARNING, ERROR, CRITICAL)"
    )


@pytest.fixture(scope="session")
def loguru_logger(request):
    """Loguru logger"""
    log_level = request.config.getoption("--loguru-level")
    logger.remove()
    logger.add(
        sys.stderr,
        level=log_level,
        format="{time:HH:mm:ss} | {level: <8} | {message}"
    )
    return logger
