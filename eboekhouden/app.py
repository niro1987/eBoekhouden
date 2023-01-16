"""Interactie met e-Boekhouden.nl"""
from datetime import datetime
from functools import cache
import logging
from typing import Any, OrderedDict

from dataclass_factory import Factory, Schema
import zeep
from zeep.helpers import serialize_object

from eboekhouden import models
from eboekhouden.model import ModelBase

from .const import DATETIME_SCHEMA, WSDL

_LOGGER: logging.Logger = logging.getLogger(__name__)


def serialize_response(response):
    """Serialized response."""
    error: OrderedDict
    (_, error), (_, response_data) = serialize_object(response).items()

    if error:
        error_message: str = error.pop("LastErrorDescription")
        _LOGGER.error(error_message)
        raise Exception(error_message)

    _LOGGER.debug("Serialized response: %s", response_data)
    return response_data


@cache
def get_factory() -> Factory:
    """Returns Factory with all required schemas."""
    return Factory(
        schemas={
            **{
                cls: Schema(
                    name_mapping=cls.name_mapping(),
                    omit_default=True,
                    pre_parse=cls.pre_parse,
                    post_serialize=cls.post_serialize,
                )
                for cls in [
                    getattr(models, class_name) for class_name in models.__all__
                ]
                if issubclass(cls, ModelBase)
            },
            datetime: DATETIME_SCHEMA,
        },
    )


def to_object(data: OrderedDict) -> list[Any]:
    """Convert serialized response to object."""
    name: str
    items: list[OrderedDict]
    name, items = data.popitem()
    # Trim the leading 'c' and trailing 'List' if applicable.
    class_name: str = name[1:-4] if name.endswith("List") else name[1:]

    cls: ModelBase
    if cls := getattr(models, class_name):
        factory: Factory = get_factory()
        instances: list[Any] = factory.load(items, list[cls])
        _LOGGER.info("%s: %s", cls.__name__, instances)
        return instances
    raise KeyError(f"No model for '{class_name}'")


def from_object(instance: ModelBase) -> dict[str, Any]:
    """Serialize model object."""
    factory: Factory = get_factory()
    cls: ModelBase = instance.__class__
    if cls in factory.schemas:
        serialized = factory.dump(instance, cls)
        _LOGGER.info("%s: %s", cls.__name__, serialized)
        return serialized
    raise KeyError(f"No model for '{cls.__name__}'")


class App:
    """Interactie met e-Boekhouden.nl."""

    def __init__(
        self,
        username: str,
        security_code_1: str,
        security_code_2: str,
    ) -> None:
        """Nieuwe App starten."""
        self.username: str = username
        self.security_code_1: str = security_code_1
        self.security_code_2: str = security_code_2

        self.client: zeep.Client = zeep.Client(WSDL)
        self.session_id: str | None = None

    def __enter__(self) -> None:
        """Context Manager."""
        self.open_session()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        """Sluit de Context Manager."""
        self.close_session()

    def open_session(self) -> None:
        """Open een sessie met e-Boekhouden."""
        response = self.client.service.OpenSession(
            Username=self.username,
            SecurityCode1=self.security_code_1,
            SecurityCode2=self.security_code_2,
        )
        serialized = serialize_response(response)
        self.session_id = serialized
        _LOGGER.info("Sessie gestart: %s", self.session_id)

    def close_session(self) -> None:
        """Sluit de sessie met e-Boekhouden."""
        if self.session_id:
            self.client.service.CloseSession(SessionID=self.session_id)
            _LOGGER.info("Sessie gesloten: %s", self.session_id)
            self.session_id = None

    def get_administraties(self) -> list[models.Administratie]:
        """Een mogelijkheid om de gekoppelde administraties op te halen."""
        response = self.client.service.GetAdministraties(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_artikelen(
        self,
        *,
        artikel_id: int | None = None,
        artikel_code: str | None = None,
        artikel_omschrijving: str | None = None,
        groep_code: str | None = None,
        groep_omschrijving: str | None = None,
    ) -> list[models.Artikel]:
        """
        Een mogelijkheid om de artikelen van een administratie op te vragen.

        Parameters
        ----------
        artikel_id : int
            Zoek op `artikel_id`.
        artikel_code : str
            Zoek op `artikel_code`.
        artikel_omschrijving : str
            Zoek op `artikel_omschrijving`.
        groep_code : str
            Zoek op `groep_code`.
        groep_omschrijving : str
            Zoek op `groep_omschrijving`.

        Returns
        -------
        list[Artikel]
            Lijst van overeenkomende artikelen.
        """
        filters: dict[str, str] = {"ArtikelID": artikel_id or 0}
        if artikel_code:
            filters["ArtikelCode"] = artikel_code
        if artikel_omschrijving:
            filters["ArtikelOmschrijving"] = artikel_omschrijving
        if groep_code:
            filters["GroepCode"] = groep_code
        if groep_omschrijving:
            filters["GroepOmschrijving"] = groep_omschrijving
        response = self.client.service.GetArtikelen(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=filters,
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_facturen(
        self,
        *,
        factuurnummer: str | None = None,
        relatiecode: str | None = None,
        start_datum: datetime | None = None,
        eind_datum: datetime | None = None,
    ) -> list[models.Factuur]:
        """
        Haalt één of meerdere facturen op.

        Parameters
        ----------
        factuurnummer : str
            Zoek op `factuurnummer`.
        relatiecode : str
            Zoek op `relatiecode`,
            gebruik in combinatie met `start_datum` en `eind_datum`.
        start_datum : datetime
            Zoek op `factuurdatum`,
            verplicht in combinatie met `relatiecode` of `eind_datum`.
        eind_datum : datetime
            Zoek op `factuurdatum`,
            verplicht in combinatie met `relatiecode` of `eind_datum`.

        Returns
        -------
        list[Factuur]
            Lijst van overeenkomende facturen.
        """
        if relatiecode and not (start_datum and eind_datum):
            raise ValueError(
                "Parameter `relatiecode` moet altijd gebruikt worden in combinatie met "
                "`start_datum` en `eind_datum`."
            )
        if (start_datum or eind_datum) and not (start_datum and eind_datum):
            raise ValueError(
                "Parameter `start_datum` en `eind_datum` moeten altijd in combinatie "
                "met elkaar gebruikt worden."
            )
        filters: dict[str, str] = {}
        if factuurnummer:
            filters["Factuurnummer"] = factuurnummer
        if relatiecode:
            filters["Relatiecode"] = relatiecode
        if start_datum:
            filters["DatumVan"] = start_datum
        if eind_datum:
            filters["DatumTm"] = eind_datum
        response = self.client.service.GetFacturen(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=filters if filters else [],
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_grootboekrekeningen(self) -> list[models.Grootboekrekening]:
        """Hiermee kunt u een lijst met grootboekrekeningen opvragen."""
        response = self.client.service.GetGrootboekrekeningen(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=[],
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_kostenplaatsen(self) -> list[models.Kostenplaats]:
        """Hiermee kunt u een lijst met kostenplaatsen opvragen."""
        response = self.client.service.GetKostenplaatsen(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=[],
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_mutaties(self) -> list[models.Mutatie]:
        """
        Hiermee kunt u een lijst met mutaties ophalen.

        Er zullen nooit meer dan de laatste 500 mutaties opgehaald worden.
        Voor deze functie geldt een maximum van 5.000 calls per maand.
        """
        response = self.client.service.GetMutaties(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=[],
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_open_posten(self, soort: str) -> list[models.OpenPost]:
        """
        Haalt een lijst op met openstaande posten van de debiteuren óf crediteuren.

        Parameters
        ----------
        soort : str
            `Debiteuren` of `Crediteuren`
        """
        if soort not in ("Debiteuren", "Crediteuren"):
            raise IndexError(
                f"'{soort}' is niet een geldige optie."
                "Gebruik 'Debiteuren' of 'Crediteuren'."
            )
        response = self.client.service.GetOpenPosten(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            OpSoort=soort,
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_relaties(
        self,
        *,
        relatie_id: int | None = None,  # pylint: disable=invalid-name,redefined-builtin
        trefwoord: str | None = None,
        code: str | None = None,
    ) -> list[models.Relatie]:
        """
        Hiermee kunt u een enkele of een lijst relaties ophalen uit het systeem.

        Parameters
        ----------
        relatie_id : int
            Zoek op `relatie_id`.
        code : str
            Zoek op `code`.
        trefwoord : str
            Zoekt in de velden `code`, `bedrijfsnaam`, `plaats`, `contactpersoon`,
            `e-mailadres` en `soort`.

        Returns
        -------
        list[Relatie]
            Lijst van overeenkomende relaties.
        """
        filters: dict[str, str] = {"ID": relatie_id or 0}
        if trefwoord:
            filters["Trefwoord"] = trefwoord
        if code:
            filters["Code"] = code
        response = self.client.service.GetRelaties(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=filters,
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_saldi(self) -> list[models.Saldo]:
        """Geeft één of meerdere saldi terug van specifieke grootboekrekeningen."""
        response = self.client.service.GetSaldi(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter=[],
        )
        serialized = serialize_response(response)
        return to_object(serialized) if serialized else []

    def get_saldo(self, grootboek_code: str, kostenplaats_id: int = 0) -> float:
        """
        Geeft de saldo terug voor een specifieke grootboekrekening of kostenplaats.
        """
        response = self.client.service.GetSaldo(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            cFilter={
                "GbCode": grootboek_code,
                "KostenPlaatsId": kostenplaats_id,
            },
        )
        _LOGGER.debug("Saldo: %s", response["Saldo"])
        return response["Saldo"]

    def add_relatie(self, relatie: models.Relatie) -> int:
        """Hiermee kunt u een relatie toevoegen aan het systeem."""
        serialized_object = from_object(relatie)
        response = self.client.service.AddRelatie(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            oRel=serialized_object,
        )
        serialized = serialize_response(response)
        _LOGGER.info("ID: %s", serialized)
        return serialized

    def add_mutatie(self, relatie: models.Mutatie) -> int:
        """Hiermee kunt u een mutatie toevoegen aan het systeem."""
        serialized_object = from_object(relatie)
        response = self.client.service.AddMutatie(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            oMut=serialized_object,
        )
        serialized = serialize_response(response)
        _LOGGER.info("ID: %s", serialized)
        return serialized

    def add_factuur(self, factuur: models.Factuur) -> str:
        """
        Hiermee voert u een nieuwe factuur in.

        Let op! Wilt u bestellingen/facturen vanuit een ander facturatiesysteem
        plaatsen, gebruik dan `add_mutatie()`.
        """
        serialized_object = from_object(factuur)
        response = self.client.service.AddFactuur(
            SessionID=self.session_id,
            SecurityCode2=self.security_code_2,
            oFact=serialized_object,
        )
        serialized = serialize_response(response)
        _LOGGER.info("ID: %s", serialized)
        return serialized
