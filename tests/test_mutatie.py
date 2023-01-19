"""Tests e-Boekhouden Relatie"""

from datetime import datetime
import os

import pytest

from eboekhouden import App, Mutatie

USERNAME: str = os.environ.get("USERNAME")
SECURITY_CODE_1: str = os.environ.get("SECURITY_CODE_1")
SECURITY_CODE_2: str = os.environ.get("SECURITY_CODE_2")


def test_get_mutaties():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        mutaties = app.get_mutaties()
        assert isinstance(mutaties, list)
        assert len(mutaties) > 0
        assert all(isinstance(item, Mutatie) for item in mutaties)


def test_get_mutatie_id():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_mutaties: list[Mutatie] = app.get_mutaties()
        mutatie_nr: int = pre_mutaties[0].mutatie_nr
        mutaties: list[Mutatie] = app.get_mutaties(mutatie_nr=mutatie_nr)
        assert all(item.mutatie_nr == mutatie_nr for item in mutaties)


def test_get_mutatie_van():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_mutaties: list[Mutatie] = app.get_mutaties()
        mutatie_nr_van: str = min([item.mutatie_nr for item in pre_mutaties])
        mutaties: list[Mutatie] = app.get_mutaties(mutatie_nr_van=mutatie_nr_van)
        assert all(item.mutatie_nr >= mutatie_nr_van for item in mutaties)


def test_get_mutatie_tot():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_mutaties: list[Mutatie] = app.get_mutaties()
        mutatie_nr_tot: str = max([item.mutatie_nr for item in pre_mutaties])
        mutaties: list[Mutatie] = app.get_mutaties(mutatie_nr_tot=mutatie_nr_tot)
        assert all(item.mutatie_nr <= mutatie_nr_tot for item in mutaties)


def test_get_mutatie_van_tot():
    """Test mutaties ophalen."""
    app: App
    with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
        pre_mutaties: list[Mutatie] = app.get_mutaties()
        mutatie_nr_van: int = min([item.mutatie_nr for item in pre_mutaties])
        mutatie_nr_tot: int = max([item.mutatie_nr for item in pre_mutaties])
        mutaties: list[Mutatie] = app.get_mutaties(
            mutatie_nr_van=mutatie_nr_van,
            mutatie_nr_tot=mutatie_nr_tot,
        )
        assert all(item.mutatie_nr >= mutatie_nr_van for item in mutaties)
        assert all(item.mutatie_nr <= mutatie_nr_tot for item in mutaties)


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
