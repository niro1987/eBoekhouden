"""Factuur model."""

from dataclasses import dataclass
from datetime import datetime

from eboekhouden.model import ModelBase
from eboekhouden.types import BTWCode, Eenheid, IncassoMachtigingSoort

NAME_MAPPING: dict[str, str] = {
    "factuurnummer": "Factuurnummer",
    "relatiecode": "Relatiecode",
    "datum": "Datum",
    "betalingstermijn": "Betalingstermijn",
    "factuursjabloon": "Factuursjabloon",
    "per_email_verzenden": "PerEmailVerzenden",
    "email_onderwerp": "EmailOnderwerp",
    "email_bericht": "EmailBericht",
    "email_van_adres": "EmailVanAdres",
    "email_van_naam": "EmailVanNaam",
    "automatische_incasso": "AutomatischeIncasso",
    "incasso_iban": "IncassoIBAN",
    "incasso_machtiging_soort": "IncassoMachtigingSoort",
    "incasso_machtiging_id": "IncassoMachtigingID",
    "incasso_machtiging_datum_ondertekening": "IncassoMachtigingDatumOndertekening",
    "incasso_machtiging_first": "IncassoMachtigingFirst",
    "incasso_rekening_nummer": "IncassoRekeningNummer",
    "incasso_tnv": "IncassoTnv",
    "incasso_plaats": "IncassoPlaats",
    "incasso_omschrijving_regel1": "IncassoOmschrijvingRegel1",
    "incasso_omschrijving_regel2": "IncassoOmschrijvingRegel2",
    "incasso_omschrijving_regel3": "IncassoOmschrijvingRegel3",
    "in_boekhouding_plaatsen": "InBoekhoudingPlaatsen",
    "boekhoudmutatie_omschrijving": "BoekhoudmutatieOmschrijving",
    "regels": "Regels",
}
NAME_MAPPING_REGEL: dict[str, str] = {
    "aantal": "Aantal",
    "eenheid": "Eenheid",
    "code": "Code",
    "omschrijving": "Omschrijving",
    "prijs_per_eenheid": "PrijsPerEenheid",
    "btw_code": "BTWCode",
    "tegenrekening_code": "TegenrekeningCode",
    "kostenplaats_id": "KostenplaatsID",
}


@dataclass
class FactuurRegel(ModelBase):  # pylint: disable=too-many-instance-attributes
    """Factuur Regel"""

    aantal: float | None = None
    eenheid: Eenheid | None = None
    code: str | None = None
    omschrijving: str | None = None
    prijs_per_eenheid: float | None = None
    btw_code: BTWCode | None = None
    tegenrekening_code: str | None = None
    kostenplaats_id: int | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING_REGEL

    def __post_init__(self):
        self.kostenplaats_id = self.kostenplaats_id or 0


@dataclass
class Factuur(ModelBase):  # pylint: disable=too-many-instance-attributes
    """Factuur"""

    relatiecode: str
    datum: datetime
    regels: list[FactuurRegel]
    factuursjabloon: str | None = None
    factuurnummer: str | None = None
    betalingstermijn: int | None = None
    per_email_verzenden: bool | None = None
    email_onderwerp: str | None = None
    email_bericht: str | None = None
    email_van_adres: str | None = None
    email_van_naam: str | None = None
    automatische_incasso: bool | None = None
    incasso_iban: str | None = None
    incasso_machtiging_soort: IncassoMachtigingSoort | None = None
    incasso_machtiging_id: str | None = None
    incasso_machtiging_datum_ondertekening: datetime | None = None
    incasso_machtiging_first: bool | None = None
    incasso_rekening_nummer: str | None = None
    incasso_tnv: str | None = None
    incasso_plaats: str | None = None
    incasso_omschrijving_regel1: str | None = None
    incasso_omschrijving_regel2: str | None = None
    incasso_omschrijving_regel3: str | None = None
    in_boekhouding_plaatsen: bool | None = None
    boekhoudmutatie_omschrijving: str | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING

    @staticmethod
    def pre_parse(data):
        data["Regels"] = data["Regels"].pop("cFactuurRegel")
        return data

    @staticmethod
    def post_serialize(data):
        data["Regels"] = {"cFactuurRegel": data["Regels"]}
        return data

    def __post_init__(self):
        self.incasso_machtiging_datum_ondertekening = (
            self.incasso_machtiging_datum_ondertekening or datetime.today()
        )
        self.incasso_machtiging_first = (
            self.incasso_machtiging_first
            if self.incasso_machtiging_first is not None
            else False
        )
        self.factuursjabloon = self.factuursjabloon or "Factuursjabloon"
