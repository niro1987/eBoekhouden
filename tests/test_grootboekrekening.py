"""Tests for the e-Boekhouden Client"""

import os

from eboekhouden import App

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_grootboekrekeningen():
    """Test het gebruik van de get_grootboekrekeningen functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_grootboekrekeningen()
        assert isinstance(data, list)
