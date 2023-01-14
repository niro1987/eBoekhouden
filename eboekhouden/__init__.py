"""e-Boekhouden API"""

import logging

from .app import App

logging.getLogger("zeep").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)

__all__ = [
    "App",
]
