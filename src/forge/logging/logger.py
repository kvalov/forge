from __future__ import annotations

import logging
import sys

import structlog

from forge.config.settings import settings

_configured = False


def configure_logging() -> None:
    """Configure Forge logging once."""

    global _configured

    if _configured:
        return

    level = getattr(logging, settings.log_level.upper(), logging.INFO)

    #
    # Root logger
    #
    logging.basicConfig(
        level=level,
        stream=sys.stdout,
        format="%(message)s",
        force=True,
    )

    #
    # Silence noisy third-party libraries.
    #
    noisy_loggers = (
        "git",
        "git.cmd",
        "urllib3",
        "httpx",
        "asyncio",
        "watchfiles",
    )

    for logger_name in noisy_loggers:
        logging.getLogger(logger_name).setLevel(logging.WARNING)

    #
    # Configure Forge logging.
    #
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(
                fmt="%Y-%m-%d %H:%M:%S"
            ),
            structlog.processors.add_log_level,
            structlog.dev.ConsoleRenderer(colors=True),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(level),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )

    _configured = True


def get_logger(name: str):
    """Return a configured Forge logger."""
    configure_logging()
    return structlog.get_logger(name)