"""Saldo model."""

from dataclasses import dataclass

from eboekhouden.model import ModelBase

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
    categorie: str | None = None
    saldo: float | None = None

    @staticmethod
    def name_mapping() -> dict:
        return NAME_MAPPING
