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


def test_invalid_credentials():
    """Test de reactie indien er ongeldige credentials worden meegegeven."""
    with pytest.raises(Exception):
        with App("USERNAME", "SECURITY_CODE_1", "SECURITY_CODE_2") as app:
            assert app.session_id is None
        assert app.session_id is None
