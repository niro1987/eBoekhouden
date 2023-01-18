"""Tests for the e-Boekhouden Client"""

import os

from eboekhouden import App

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_open_posten_deb():
    """Test het gebruik van de get_open_posten functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_open_posten_debiteuren()
        assert isinstance(data, list)


def test_get_open_posten_cred():
    """Test het gebruik van de get_open_posten functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_open_posten_crediteuren()
        assert isinstance(data, list)
