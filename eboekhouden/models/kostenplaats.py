"""Kostenplaats model."""

from dataclasses import dataclass

from eboekhouden.model import Model

NAME_MAPPING: dict[str, str] = {
    "kostenplaats_id": "KostenplaatsId",
    "omschrijving": "Omschrijving",
    "kostenplaats_parent_id": "KostenplaatsParentId",
}


@dataclass
class Kostenplaats(Model):
    """Kostenplaats."""

    kostenplaats_id: int | None = None
    omschrijving: str | None = None
    kostenplaats_parent_id: int | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
