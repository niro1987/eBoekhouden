"""Artikel  model."""

from dataclasses import dataclass

from eboekhouden.model import ModelBase

NAME_MAPPING: dict[str, str] = {
    "artikel_id": "ArtikelID",
    "artikel_omschrijving": "ArtikelOmschrijving",
    "artikel_code": "ArtikelCode",
    "groep_omschrijving": "GroepOmschrijving",
    "groep_code": "GroepCode",
    "eenheid": "Eenheid",
    "inkoopprijs_excl_btw": "InkoopprijsExclBTW",
    "verkoopprijs_excl_btw": "VerkoopprijsExclBTW",
    "verkoopprijs_incl_btw": "VerkoopprijsInclBTW",
    "btw_code": "BTWCode",
    "tegenrekening_code": "TegenrekeningCode",
    "btw_percentage": "BtwPercentage",
    "kostenplaats_id": "KostenplaatsID",
    "actief": "Actief",
}


@dataclass
class Artikel(ModelBase):  # pylint: disable=too-many-instance-attributes
    """Artikel."""

    artikel_id: int | None = None
    artikel_omschrijving: str | None = None
    artikel_code: str | None = None
    groep_omschrijving: str | None = None
    groep_code: str | None = None
    eenheid: str | None = None
    inkoopprijs_excl_btw: float | None = None
    verkoopprijs_excl_btw: float | None = None
    verkoopprijs_incl_btw: float | None = None
    btw_code: str | None = None
    tegenrekening_code: str | None = None
    btw_percentage: float | None = None
    kostenplaats_id: int | None = None
    actief: bool | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
