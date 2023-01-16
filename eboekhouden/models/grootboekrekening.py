"""Grootboekrekening model."""

from dataclasses import dataclass

from eboekhouden.model import ModelBase

NAME_MAPPING: dict[str, str] = {
    "id": "ID",
    "code": "Code",
    "omschrijving": "Omschrijving",
    "categorie": "Categorie",
    "groep": "Groep",
}


@dataclass
class Grootboekrekening(ModelBase):
    """Grootboekrekening."""

    id: int | None = None  # pylint: disable=invalid-name
    code: str | None = None
    omschrijving: str | None = None
    categorie: str | None = None
    groep: str | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
