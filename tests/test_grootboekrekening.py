"""Tests for the e-Boekhouden Client"""

import os

from eboekhouden import App, Grootboekrekening

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_grootboekrekeningen():
    """Test het gebruik van de get_grootboekrekeningen functie."""
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        grootboekrekeningen = app.get_grootboekrekeningen()
        assert isinstance(grootboekrekeningen, list)
        assert len(grootboekrekeningen) > 0
        assert all(isinstance(item, Grootboekrekening) for item in grootboekrekeningen)
