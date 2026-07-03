from forge.logging.logger import get_logger


def test_logger_creation():
    logger = get_logger(__name__)
    assert logger is not None