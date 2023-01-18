"""Mutatie Soort"""
from enum import Enum


class MutatieSoort(Enum):
    """Mutatie Soort"""

    FACTUUR_ONTVANGEN = "FactuurOntvangen"
    """Factuur ontvangen"""

    FACTUUR_VERSTUURD = "FactuurVerstuurd"
    """Factuur verstuurd"""

    FACTUUR_BETALING_ONTVANGEN = "FactuurbetalingOntvangen"
    """Factuurbetaling ontvangen"""

    FACTUUR_BETALING_VERSTUURD = "FactuurbetalingVerstuurd"
    """Factuurbetaling verstuurd"""

    GELD_ONTVANGEN = "GeldOntvangen"
    """Geld ontvangen"""

    GELD_UITGEGEVEN = "GeldUitgegeven"
    """Geld uitgegeven"""

    MEMORIAAL = "Memoriaal"
    """Memoriaal"""
