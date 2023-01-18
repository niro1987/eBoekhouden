"""Eenheid"""
from enum import Enum


class GrootboekCategorie(Enum):
    """Categorie van een grootboekrekening."""

    BALANS = "BAL"
    """Balans"""

    WINST_EN_VERLIES = "VW"
    """Winst & Verlies"""

    BETAALMIDDELEN = "FIN"
    """Betalingsmiddelen"""

    BTW_LAAG = "AF6"
    """BTW af te dragen Laag"""

    BTW_HOOG = "AF19"
    """BTW af te dragen Hoog"""

    BTW_OVERIG = "AFOVERIG"
    """BTW af te dragen overig"""

    BTWRC = "BTWRC"
    """BTW Rekening Courant"""

    DEBITEUR = "DEB"
    """Debiteuren"""

    CREDITEUR = "CRED"
    """Crediteuren"""

    VOORBELASTING = "VOOR"
    """Voorbelasting"""
