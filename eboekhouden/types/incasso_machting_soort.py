"""Incasso Machtiging Soort"""
from enum import Enum


class IncassoMachtigingSoort(Enum):
    """Incasso Machtiging Soort"""

    EENMALIG = "E"
    """Eenmalige machtiging"""

    DOORLOPEND = "D"
    """Doorlopende machtiging"""
