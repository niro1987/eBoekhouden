"""Model base class for all eBoekhouden data models."""
from abc import ABC, abstractmethod


class Model(ABC):  # pylint: disable=too-few-public-methods
    """Basis class voor modellen."""

    @staticmethod
    @abstractmethod
    def name_mapping() -> dict:
        """name mapping for this schema."""

    @staticmethod
    def pre_parse(data):
        """pre_parse for this schema."""
        return data

    @staticmethod
    def post_serialize(data):
        """post_serialize for this schema."""
        return data
