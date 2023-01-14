"""Mutatie Soort"""
from enum import Enum


class MutatieSoort(Enum):
    """Mutatie Soort"""

    FACTUUR_ONTVANGEN = "FactuurOntvangen"
    """FactuurOntvangen"""

    FACTUUR_VERSTUURD = "FactuurVerstuurd"
    """FactuurVerstuurd"""

    FACTUUR_BETALING_ONTVANGEN = "FactuurbetalingOntvangen"
    """FactuurbetalingOntvangen"""

    FACTUUR_BETALING_VERSTUURD = "FactuurbetalingVerstuurd"
    """FactuurbetalingVerstuurd"""

    GELD_ONTVANGEN = "GeldOntvangen"
    """GeldOntvangen"""

    GELD_UITGEGEVEN = "GeldUitgegeven"
    """GeldUitgegeven"""

    MEMORIAAL = "Memoriaal"
    """Memoriaal"""
