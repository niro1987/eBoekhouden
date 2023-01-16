"""Kostenplaats model."""

from dataclasses import dataclass

from eboekhouden.model import ModelBase

NAME_MAPPING: dict[str, str] = {
    "kostenplaats_id": "KostenplaatsId",
    "omschrijving": "Omschrijving",
    "kostenplaats_parent_id": "KostenplaatsParentId",
}


@dataclass
class Kostenplaats(ModelBase):
    """Kostenplaats."""

    kostenplaats_id: int | None = None
    omschrijving: str | None = None
    kostenplaats_parent_id: int | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
