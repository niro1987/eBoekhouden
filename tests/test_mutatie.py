"""Tests e-Boekhouden Relatie"""

from datetime import datetime
import os

import pytest

from eboekhouden import App, BTWCode, InExBTW, Mutatie, MutatieRegel, MutatieSoort

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_mutaties():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_mutaties()
        assert isinstance(data, list)


def test_get_mutatie_id():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_mutaties(mutatienummer=9)
        assert isinstance(data, list)


def test_get_mutatie_van_tot():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_mutaties(mutatienummer_van=19, mutatienummer_tot=20)
        assert isinstance(data, list)
        assert len(data) == 2


def test_get_mutatie_factuurnummer():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_mutaties(factuurnummer="F00007")
        assert isinstance(data, list)


def test_get_mutatie_datum_range():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        data = app.get_mutaties(
            start_datum=datetime.today().date(),
            eind_datum=datetime.today().date(),
        )
        assert isinstance(data, list)


def test_get_mutatie_datum_range_invalid():
    """Test mutaties ophalen."""
    app: App
    with pytest.raises(ValueError):
        with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
            data = app.get_mutaties(
                start_datum=datetime.today().date(),
            )
            assert isinstance(data, list)


def test_add_mutatie_geld_ontvangen():
    """Test mutatie toevoegen Geld Ontvangen."""
    new_mutatie: Mutatie = Mutatie(
        soort=MutatieSoort.GELD_ONTVANGEN,
        datum=datetime.today(),
        rekening="1000",  # Kas
        omschrijving="SPAM_EGGS",
        in_ex_btw=InExBTW.EX,
        mutaties=[
            MutatieRegel(
                bedrag_invoer=1,
                bedrag_excl_btw=1,
                bedrag_btw=0.21,
                bedrag_incl_btw=1.21,
                btw_percentage=21,
                btw_code=BTWCode.HOOG_VERK_21,
                tegenrekening_code="1400",  # Eigen vermogen
            ),
        ],
    )
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        app.add_mutatie(new_mutatie)
