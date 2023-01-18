"""Tests for the e-Boekhouden Client"""

import os

from eboekhouden import App

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_administraties():
    """Test het gebruik van de get_administraties functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_administraties()
        assert isinstance(data, list)
