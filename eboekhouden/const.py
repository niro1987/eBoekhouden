"""Constants for e-Boekhouden"""
from dataclass_factory import Schema

WSDL: str = "https://soap.e-boekhouden.nl/soap.asmx?wsdl"


# Custom Schemas
DATETIME_SCHEMA: Schema = Schema(
    parser=lambda x: x,
    serializer=lambda x: x,
)
MUTATIE_LIST_SCHEMA: Schema = Schema(
    parser=lambda x: x["cMutatieListRegel"],
    serializer=lambda x: {"cMutatieRegel": x},
)
