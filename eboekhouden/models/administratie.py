"""Administratie model."""

from dataclasses import dataclass
from datetime import date, datetime

from eboekhouden.model import ModelBase

NAME_MAPPING: dict[str, str] = {
    "bedrijf": "Bedrijf",
    "plaats": "Plaats",
    "guid": "Guid",
    "start_boekjaar": "StartBoekjaar",
}


@dataclass
class Administratie(ModelBase):
    """Administratie."""

    bedrijf: str | None = None
    plaats: str | None = None
    guid: str | None = None
    start_boekjaar: date | datetime | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
