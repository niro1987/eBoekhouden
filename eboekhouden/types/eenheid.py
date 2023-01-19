"""Eenheid"""
from enum import Enum


class Eenheid(Enum):
    """Eenheid van het artikel."""

    STUK = "stuk"
    """Per stuk"""

    DOOS = "doos"
    """Per doos"""

    UUR = "uur"
    """Per uur"""
