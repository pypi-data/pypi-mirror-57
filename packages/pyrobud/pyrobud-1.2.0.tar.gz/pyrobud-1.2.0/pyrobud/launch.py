import asyncio
import logging

import colorlog
import toml

from . import util
from .bot import Bot

LOG_LEVEL = logging.INFO
LOG_FORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(name)-7s | %(log_color)s%(message)s%(reset)s"

log = logging.getLogger("launch")


def setup_logging():
    logging.root.setLevel(LOG_LEVEL)
    formatter = colorlog.ColoredFormatter(LOG_FORMAT)

    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(LOG_LEVEL)
    root.addHandler(stream)


def setup_loop():
    # While uvloop is in our requirements.txt, it's not required by any means
    # and doesn't work in Termux due to their patched libuv
    try:
        import uvloop

        uvloop.install()
    except ImportError:
        log.warn("Unable to load uvloop; falling back to default asyncio event loop")


def main():
    config_path = "config.toml"

    setup_logging()
    setup_loop()

    log.info("Loading config")
    config = toml.load(config_path)

    # Initialize Sentry reporting here to exempt config syntax errors and query
    # the user's report_errors value, defaulting to enabled if not specified
    if config["bot"].get("report_errors", True):
        log.info("Initializing Sentry error reporting")
        util.sentry.init()

    util.config.upgrade(config, config_path)

    log.info("Initializing bot")
    bot = Bot(config)

    log.info("Starting bot")
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(bot.start())
    except KeyboardInterrupt:
        log.warn("Received interrupt while connecting; exiting")
        return

    bot.client.run_until_disconnected()

    log.info("Stopping bot")
    loop.run_until_complete(bot.stop())


if __name__ == "__main__":
    main()
