"""Tests e-Boekhouden Relatie"""

from datetime import datetime
import os

from eboekhouden.app import App
from eboekhouden.models import Factuur, FactuurRegel
from eboekhouden.types import BTWCode, Eenheid

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_facturen():
    """Test facturen ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        facturen = app.get_facturen()
        assert isinstance(facturen, list)
        assert all(isinstance(item, Factuur) for item in facturen)


def test_get_factuur_factuurnummer():
    """Test factuur ophalen op factuurnummer."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        facturen: list[Factuur] = app.get_facturen(factuurnummer="F00007")
        assert isinstance(facturen, list)
        assert all(factuur.factuurnummer == "F00007" for factuur in facturen)


def test_get_factuur_relatiecode():
    """Test factuur ophalen op relatiecode."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        facturen: list[Factuur] = app.get_facturen(
            relatiecode="R0002",
            start_datum=datetime(2000, 1, 1),
            eind_datum=datetime(2200, 1, 1),
        )
        assert isinstance(facturen, list)
        assert all(factuur.relatiecode == "R0002" for factuur in facturen)


def test_get_factuur_datum_range():
    """Test factuur ophalen op relatiecode."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        start_datum: datetime = datetime(2000, 1, 1)
        eind_datum: datetime = datetime(2200, 1, 1)
        facturen: list[Factuur] = app.get_facturen(
            start_datum=start_datum,
            eind_datum=eind_datum,
        )
        assert isinstance(facturen, list)
        assert all(isinstance(factuur, Factuur) for factuur in facturen)
        assert all(factuur.datum >= start_datum for factuur in facturen)
        assert all(factuur.datum <= eind_datum for factuur in facturen)


def test_add_factuur_geen_email():
    """Test factuur toevoegen zonder per email te versturen."""
    new_factuur: Factuur = Factuur(
        relatiecode="SPAM",
        datum=datetime.today(),
        betalingstermijn="14",
        per_email_verzenden=False,
        automatische_incasso=False,
        in_boekhouding_plaatsen=False,
        regels=[
            FactuurRegel(
                code="SPAM",
                omschrijving="EGGS",
                aantal=1,
                eenheid=Eenheid.UUR,
                prijs_per_eenheid=100,
                btw_code=BTWCode.HOOG_VERK_21,
                tegenrekening_code="1400",
            ),
        ],
    )
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        app.add_factuur(new_factuur)


def test_add_factuur_wel_email():
    """Test factuur toevoegen zonder per email te versturen."""
    new_factuur: Factuur = Factuur(
        relatiecode="SPAM",
        datum=datetime.today(),
        betalingstermijn="14",
        per_email_verzenden=True,
        email_onderwerp="Factuur",
        email_van_adres="niels.perfors1987@gmail.com",
        email_bericht="test bericht",
        automatische_incasso=False,
        in_boekhouding_plaatsen=True,
        boekhoudmutatie_omschrijving="factuur",
        regels=[
            FactuurRegel(
                code="SPAM",
                omschrijving="EGGS",
                aantal=1,
                eenheid=Eenheid.UUR,
                prijs_per_eenheid=100,
                btw_code=BTWCode.HOOG_VERK_21,
                tegenrekening_code="1400",
            ),
        ],
    )
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        app.add_factuur(new_factuur)
