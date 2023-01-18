"""Tests for the e-Boekhouden Client"""

import os

import pytest

from eboekhouden import App

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_saldo():
    """Test het gebruik van de get_saldo functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_saldo("1000")  # Kas
        assert isinstance(data, float)


def test_get_saldo_wrong_account():
    """Test het gebruik van de get_saldo functie."""
    with pytest.raises(Exception):
        with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
            data = app.get_saldo("0")  # Does not exist
            assert isinstance(data, float)
