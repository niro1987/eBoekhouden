"""Tests e-Boekhouden Relatie"""

import os

from eboekhouden import App, Relatie, RelatieType

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_relaties():
    """Test relaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        relaties: list[Relatie] = app.get_relaties()
        assert isinstance(relaties, list)
        assert all(isinstance(item, Relatie) for item in relaties)


def test_get_relatie_id():
    """Test relatie ophalen op id."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_relaties: list[Relatie] = app.get_relaties(code="SPAM")
        relatie_id: int = pre_relaties[0].relatie_id
        relaties: list[Relatie] = app.get_relaties(relatie_id=relatie_id)
        assert isinstance(relaties, list)
        assert len(relaties) == 1
        assert relaties[0].relatie_id == relatie_id


def test_get_relatie_code():
    """Test relatie ophalen op code."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        relaties: list[Relatie] = app.get_relaties(code="SPAM")
        assert isinstance(relaties, list)
        assert all(isinstance(item, Relatie) for item in relaties)
        assert len(relaties) == 1


def test_get_relatie_trefwoord():
    """Test relatie ophalen op trefwoord."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        relaties: list[Relatie] = app.get_relaties(trefwoord="EGGS")
        assert isinstance(relaties, list)
        assert all(isinstance(item, Relatie) for item in relaties)
        assert len(relaties) == 1


def test_add_relatie_particulier():
    """Test particuliere toevoegen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        new_relatie: Relatie = Relatie(
            code="SPAM",
            relatie_type=RelatieType.PARTICULIER,
            bedrijf="EGGS",
        )
        new_relatie_id: int = app.add_relatie(new_relatie)
        assert isinstance(new_relatie_id, int)

        relaties: list[Relatie] = app.get_relaties(code="SPAM")
        assert isinstance(relaties, list)
        assert all(isinstance(item, Relatie) for item in relaties)
        assert len(relaties) == 1

        relatie: Relatie = relaties[0]
        assert isinstance(relatie, Relatie)
        assert relatie.code == new_relatie.code


def test_add_relatie_bedrijf():
    """Test bedrijf toevoegen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        new_relatie: Relatie = Relatie(
            code="EGGS",
            relatie_type=RelatieType.BEDRIJF,
            bedrijf="SPAM",
        )
        new_relatie_id: int = app.add_relatie(new_relatie)
        assert isinstance(new_relatie_id, int)

        relaties: list[Relatie] = app.get_relaties(code="EGGS")
        assert isinstance(relaties, list)
        assert all(isinstance(item, Relatie) for item in relaties)
        assert len(relaties) == 1

        relatie: Relatie = relaties[0]
        assert isinstance(relatie, Relatie)
        assert relatie.code == new_relatie.code
