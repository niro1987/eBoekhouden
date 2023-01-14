"""Modellen voor e-Boekhouden"""

from eboekhouden.models.administratie import Administratie
from eboekhouden.models.artikel import Artikel
from eboekhouden.models.factuur import Factuur, FactuurRegel
from eboekhouden.models.grootboekrekening import Grootboekrekening
from eboekhouden.models.kostenplaats import Kostenplaats
from eboekhouden.models.mutatie import Mutatie, MutatieRegel
from eboekhouden.models.open_post import OpenPost
from eboekhouden.models.relatie import Relatie
from eboekhouden.models.saldo import Saldo

__all__: list[str] = [
    "Administratie",
    "Artikel",
    "Factuur",
    "FactuurRegel",
    "Grootboekrekening",
    "Kostenplaats",
    "Mutatie",
    "MutatieRegel",
    "OpenPost",
    "Relatie",
    "Saldo",
]
