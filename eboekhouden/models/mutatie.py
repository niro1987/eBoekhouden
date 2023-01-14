"""Mutatie model."""
from dataclasses import dataclass
from datetime import datetime
import logging

from eboekhouden.model import Model
from eboekhouden.types import BTWCode, InExBTW, MutatieSoort

_LOGGER: logging.Logger = logging.getLogger(__name__)
NAME_MAPPING: dict[str, str] = {
    "mutatie_nr": "MutatieNr",
    "soort": "Soort",
    "datum": "Datum",
    "rekening": "Rekening",
    "relatie_code": "RelatieCode",
    "factuurnummer": "Factuurnummer",
    "boekstuk": "Boekstuk",
    "omschrijving": "Omschrijving",
    "betalingstermijn": "Betalingstermijn",
    "betalingskenmerk": "Betalingskenmerk",
    "in_ex_btw": "InExBTW",
    # "mutaties": ("MutatieRegels", "cMutatieListRegel"),
    "mutaties": "MutatieRegels",
}
NAME_MAPPING_LIST: dict[str, str] = {
    "regels": "MutatieListRegel",
}
NAME_MAPPING_REGEL: dict[str, str] = {
    "bedrag_invoer": "BedragInvoer",
    "bedrag_excl_btw": "BedragExclBTW",
    "bedrag_btw": "BedragBTW",
    "bedrag_incl_btw": "BedragInclBTW",
    "btw_code": "BTWCode",
    "btw_percentage": "BTWPercentage",
    "tegenrekening_code": "TegenrekeningCode",
    "kostenplaats_id": "KostenplaatsID",
}


@dataclass
class MutatieRegel(Model):  # pylint: disable=too-many-instance-attributes
    """Mutatie Regel"""

    bedrag_invoer: float
    bedrag_excl_btw: float
    bedrag_btw: float
    bedrag_incl_btw: float
    btw_percentage: float | None = None
    btw_code: BTWCode | None = None
    tegenrekening_code: str | None = None
    kostenplaats_id: int | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING_REGEL

    def __post_init__(self):
        self.kostenplaats_id = self.kostenplaats_id or 0


@dataclass
class Mutatie(Model):  # pylint: disable=too-many-instance-attributes
    """Boekhoudmutatie"""

    soort: MutatieSoort
    datum: datetime
    rekening: str
    mutaties: list[MutatieRegel]
    relatie_code: str | None = None
    factuurnummer: str | None = None
    betalingstermijn: str | None = None
    mutatie_nr: int | None = None
    boekstuk: str | None = None
    omschrijving: str | None = None
    betalingskenmerk: str | None = None
    in_ex_btw: InExBTW | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING

    @staticmethod
    def pre_parse(data):
        data["MutatieRegels"] = data["MutatieRegels"].pop("cMutatieListRegel")
        return data

    @staticmethod
    def post_serialize(data):
        data["MutatieRegels"] = {"cMutatieRegel": data["MutatieRegels"]}
        return data

    def __post_init__(self):
        self.mutatie_nr = self.mutatie_nr or 0
