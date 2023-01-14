"""Tests e-Boekhouden Artikel"""

import os

from eboekhouden.app import App
from eboekhouden.models import Artikel

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_artikelen():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        artikelen: list[Artikel] = app.get_artikelen()
        assert isinstance(artikelen, list)
        assert all(isinstance(item, Artikel) for item in artikelen)


def test_get_artikel_id():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_artikelen: list[Artikel] = app.get_artikelen(artikel_code="SPAM")
        artikel_id: int = pre_artikelen[0].artikel_id
        artikelen: list[Artikel] = app.get_artikelen(artikel_id=artikel_id)
        assert isinstance(artikelen, list)
        assert len(artikelen) > 0
        assert all(isinstance(item, Artikel) for item in artikelen)
        assert all(item.artikel_id == artikel_id for item in artikelen)


def test_get_artikel_code():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        artikelen: list[Artikel] = app.get_artikelen(artikel_code="SPAM")
        assert isinstance(artikelen, list)
        assert len(artikelen) > 0
        assert all(isinstance(item, Artikel) for item in artikelen)
        assert all(item.artikel_code == "SPAM" for item in artikelen)


def test_get_artikel_omschrijving():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        artikelen: list[Artikel] = app.get_artikelen(
            artikel_omschrijving="Dummy Artikel"
        )
        assert isinstance(artikelen, list)
        assert len(artikelen) > 0
        assert all(isinstance(item, Artikel) for item in artikelen)
        assert all(item.artikel_omschrijving == "Dummy Artikel" for item in artikelen)


def test_get_artikel_groep_code():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        artikelen: list[Artikel] = app.get_artikelen(groep_code="EGGS")
        assert isinstance(artikelen, list)
        assert len(artikelen) > 0
        assert all(isinstance(item, Artikel) for item in artikelen)
        assert all(item.groep_code == "EGGS" for item in artikelen)


def test_get_artikel_groep_omschrijving():
    """Test artikelen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        artikelen: list[Artikel] = app.get_artikelen(groep_omschrijving="Dummy Groep")
        assert isinstance(artikelen, list)
        assert len(artikelen) > 0
        assert all(isinstance(item, Artikel) for item in artikelen)
        assert all(item.groep_omschrijving == "Dummy Groep" for item in artikelen)
