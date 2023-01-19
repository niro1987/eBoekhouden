"""Tests e-Boekhouden Relatie"""

from datetime import datetime
import os

from eboekhouden import App, Factuur

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_facturen():
    """Test facturen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        facturen = app.get_facturen()
        assert isinstance(facturen, list)
        assert len(facturen) > 0
        assert all(isinstance(item, Factuur) for item in facturen)


def test_get_factuur_factuurnummer():
    """Test factuur ophalen op factuurnummer."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_facturen: list[Factuur] = app.get_facturen()
        factuurnummer: str = pre_facturen[0].factuurnummer
        facturen: list[Factuur] = app.get_facturen(factuurnummer=factuurnummer)
        assert all(item.factuurnummer == factuurnummer for item in facturen)


def test_get_factuur_relatiecode():
    """Test factuur ophalen op relatiecode."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_facturen: list[Factuur] = app.get_facturen()
        relatiecode: str = pre_facturen[0].relatiecode
        facturen: list[Factuur] = app.get_facturen(relatiecode=relatiecode)
        assert all(item.relatiecode == relatiecode for item in facturen)


def test_get_factuur_datum_start():
    """Test factuur ophalen op relatiecode."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        start_datum: datetime = datetime(2000, 1, 1)
        facturen: list[Factuur] = app.get_facturen(
            start_datum=start_datum,
        )
        assert all(factuur.datum >= start_datum for factuur in facturen)


def test_get_factuur_datum_eind():
    """Test factuur ophalen op relatiecode."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        eind_datum: datetime = datetime(2200, 1, 1)
        facturen: list[Factuur] = app.get_facturen(
            eind_datum=eind_datum,
        )
        assert all(factuur.datum <= eind_datum for factuur in facturen)


def test_get_factuur_datum_range():
    """Test factuur ophalen op relatiecode."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        start_datum: datetime = datetime(2000, 1, 1)
        eind_datum: datetime = datetime(2200, 1, 1)
        facturen: list[Factuur] = app.get_facturen(
            start_datum=start_datum,
            eind_datum=eind_datum,
        )
        assert all(factuur.datum >= start_datum for factuur in facturen)
        assert all(factuur.datum <= eind_datum for factuur in facturen)
