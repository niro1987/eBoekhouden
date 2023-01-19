"""Tests e-Boekhouden Artikel"""

import os

from eboekhouden import App, Artikel

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_artikelen():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        artikelen: list[Artikel] = app.get_artikelen()
        assert isinstance(artikelen, list)
        assert len(artikelen) > 0
        assert all(isinstance(item, Artikel) for item in artikelen)


def test_get_artikel_id():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_artikelen: list[Artikel] = app.get_artikelen()
        artikel_id: int = pre_artikelen[0].artikel_id
        artikelen: list[Artikel] = app.get_artikelen(artikel_id=artikel_id)
        assert all(item.artikel_id == artikel_id for item in artikelen)


def test_get_artikel_code():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_artikelen: list[Artikel] = app.get_artikelen()
        artikel_code: str = pre_artikelen[0].artikel_code
        artikelen: list[Artikel] = app.get_artikelen(artikel_code=artikel_code)
        assert all(item.artikel_code == artikel_code for item in artikelen)


def test_get_artikel_omschrijving():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_artikelen: list[Artikel] = app.get_artikelen()
        artikel_omschrijving: str = pre_artikelen[0].artikel_omschrijving
        artikelen: list[Artikel] = app.get_artikelen(
            artikel_omschrijving=artikel_omschrijving
        )
        assert all(
            item.artikel_omschrijving == artikel_omschrijving for item in artikelen
        )


def test_get_artikel_groep_code():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_artikelen: list[Artikel] = app.get_artikelen()
        groep_code: str = pre_artikelen[0].groep_code
        artikelen: list[Artikel] = app.get_artikelen(groep_code=groep_code)
        assert all(item.groep_code == groep_code for item in artikelen)


def test_get_artikel_groep_omschrijving():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_artikelen: list[Artikel] = app.get_artikelen()
        groep_omschrijving: str = pre_artikelen[0].groep_omschrijving
        artikelen: list[Artikel] = app.get_artikelen(
            groep_omschrijving=groep_omschrijving
        )
        assert all(item.groep_omschrijving == groep_omschrijving for item in artikelen)
