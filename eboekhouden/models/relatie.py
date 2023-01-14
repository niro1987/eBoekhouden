"""Relatie model."""

from dataclasses import dataclass
from datetime import datetime

from eboekhouden.model import Model
from eboekhouden.types import RelatieType

NAME_MAPPING: dict[str, str] = {
    "relatie_id": "ID",
    "add_datum": "AddDatum",
    "code": "Code",
    "bedrijf": "Bedrijf",
    "contactpersoon": "Contactpersoon",
    "geslacht": "Geslacht",
    "adres": "Adres",
    "postcode": "Postcode",
    "plaats": "Plaats",
    "land": "Land",
    "adres_factuur": "Adres2",
    "postcode_factuur": "Postcode2",
    "plaats_factuur": "Plaats2",
    "land_factuur": "Land2",
    "telefoon": "Telefoon",
    "mobiel": "GSM",
    "fax": "FAX",
    "email": "Email",
    "site": "Site",
    "notitie": "Notitie",
    "bankrekening": "Bankrekening",
    "girorekening": "Girorekening",
    "btw_nummer": "BTWNummer",
    "kvk_nummer": "KvkNummer",
    "aanhef": "Aanhef",
    "iban": "IBAN",
    "bic": "BIC",
    "relatie_type": "BP",
    "def1": "Def1",
    "def2": "Def2",
    "def3": "Def3",
    "def4": "Def4",
    "def5": "Def5",
    "def6": "Def6",
    "def7": "Def7",
    "def8": "Def8",
    "def9": "Def9",
    "def10": "Def10",
    "la": "LA",
    "gb_id": "Gb_ID",
    "geen_email": "GeenEmail",
    "nieuwsbriefgroepen_count": "NieuwsbriefgroepenCount",
}


@dataclass
class Relatie(Model):  # pylint: disable=too-many-instance-attributes
    """Relatie."""

    relatie_type: RelatieType  # pylint: disable=invalid-name
    code: str
    relatie_id: int | None = None  # pylint: disable=invalid-name
    add_datum: datetime | None = None
    bedrijf: str | None = None
    contactpersoon: str | None = None
    geslacht: str | None = None
    adres: str | None = None
    postcode: str | None = None
    plaats: str | None = None
    land: str | None = None
    adres_factuur: str | None = None
    postcode_factuur: str | None = None
    plaats_factuur: str | None = None
    land_factuur: str | None = None
    telefoon: str | None = None
    mobiel: str | None = None
    fax: str | None = None
    email: str | None = None
    site: str | None = None
    notitie: str | None = None
    bankrekening: str | None = None
    girorekening: str | None = None
    btw_nummer: str | None = None
    kvk_nummer: str | None = None
    aanhef: str | None = None
    iban: str | None = None
    bic: str | None = None
    def1: str | None = None
    def2: str | None = None
    def3: str | None = None
    def4: str | None = None
    def5: str | None = None
    def6: str | None = None
    def7: str | None = None
    def8: str | None = None
    def9: str | None = None
    def10: str | None = None
    la: str | None = None  # pylint: disable=invalid-name
    gb_id: int | None = None
    geen_email: int | None = None
    nieuwsbriefgroepen_count: int | None = None

    @staticmethod
    def name_mapping() -> dict[str, str]:
        return NAME_MAPPING

    def __post_init__(self):
        self.relatie_id = self.relatie_id if self.relatie_id is not None else 0
        self.add_datum = self.add_datum or datetime.today()
        self.gb_id = self.gb_id if self.gb_id is not None else 0
        self.geen_email = self.geen_email if self.geen_email is not None else 0
        self.nieuwsbriefgroepen_count = (
            self.nieuwsbriefgroepen_count
            if self.nieuwsbriefgroepen_count is not None
            else 0
        )
