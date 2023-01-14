"""OpenPost model."""

from dataclasses import dataclass
from datetime import datetime

from eboekhouden.model import Model

NAME_MAPPING: dict[str, str] = {
    "mut_datum": "MutDatum",
    "mut_factuur": "MutFactuur",
    "rel_code": "RelCode",
    "rel_bedrijf": "RelBedrijf",
    "bedrag": "Bedrag",
    "voldaan": "Voldaan",
    "openstaand": "Openstaand",
}


@dataclass
class OpenPost(Model):
    """OpenPost."""

    mut_datum: datetime | None = None
    mut_factuur: str | None = None
    rel_code: str | None = None
    rel_bedrijf: str | None = None
    bedrag: float | None = None
    voldaan: float | None = None
    openstaand: float | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
