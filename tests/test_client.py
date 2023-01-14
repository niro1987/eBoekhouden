"""Tests for the e-Boekhouden Client"""

import os

import pytest

from eboekhouden import App

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_app_as_context_manager():
    """Test het gebruik van de app als context manager."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        assert app.session_id is not None
    assert app.session_id is None


def test_app_without_context_manager():
    """Test het gebruik van de app zonder context manager."""
    app = App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2)
    assert app.session_id is None
    app.open_session()
    assert app.session_id is not None
    app.close_session()
    assert app.session_id is None


def test_get_administraties():
    """Test het gebruik van de get_administraties functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_administraties()
        assert isinstance(data, list)


def test_get_artikelen():
    """Test het gebruik van de get_artikelen functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_artikelen()
        assert isinstance(data, list)


def test_get_grootboekrekeningen():
    """Test het gebruik van de get_grootboekrekeningen functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_grootboekrekeningen()
        assert isinstance(data, list)


def test_get_kostenplaatsen():
    """Test het gebruik van de get_kostenplaatsen functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_kostenplaatsen()
        assert isinstance(data, list)


def test_get_open_posten_deb():
    """Test het gebruik van de get_open_posten functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_open_posten("Debiteuren")
        assert isinstance(data, list)


def test_get_open_posten_cred():
    """Test het gebruik van de get_open_posten functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_open_posten("Debiteuren")
        assert isinstance(data, list)


def test_get_open_posten_error():
    """Test het gebruik van de get_open_posten functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        with pytest.raises(IndexError):
            app.get_open_posten("test")


def test_get_saldi():
    """Test het gebruik van de get_saldi functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_saldi()
        assert isinstance(data, list)


def test_get_saldo():
    """Test het gebruik van de get_saldo functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_saldo("1000")
        assert isinstance(data, float)
