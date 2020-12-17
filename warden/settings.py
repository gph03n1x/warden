import logging

from decouple import config
from rich.logging import RichHandler

Logger = logging.getLogger(__name__)
Logger.setLevel(logging.INFO)
Logger.addHandler(RichHandler(rich_tracebacks=True))

INTERVAL = config("INTERVAL", cast=int, default=60 * 5)
TIMEOUT = config("TIMEOUT", cast=int, default=30)
WEBHOOK = config("WEBHOOK")
