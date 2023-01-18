"""Saldo model."""

from dataclasses import dataclass

from eboekhouden.model import ModelBase
from eboekhouden.types import GrootboekCategorie

NAME_MAPPING: dict[str, str] = {
    "id": "ID",
    "code": "Code",
    "categorie": "Categorie",
    "saldo": "Saldo",
}


@dataclass
class Saldo(ModelBase):
    """Saldo."""

    id: int | None = None  # pylint: disable=invalid-name
    code: str | None = None
    categorie: GrootboekCategorie | None = None
    saldo: float | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
