"""BTW-codes"""
from enum import Enum


class BTWCode(Enum):
    """Lijst met beschikbare BTW-codes"""

    HOOG_VERK = "HOOG_VERK"
    """BTW hoog, verkopen 19%"""

    HOOG_VERK_21 = "HOOG_VERK_21"
    """BTW hoog, verkopen 21%"""

    LAAG_VERK = "LAAG_VERK"
    """
    BTW laag, verkopen

    Indien de boekdatum in 2019 of er na valt, wordt 9% aangehouden, daarvoor 6%.
    """

    LAAG_VERK_9 = "LAAG_VERK_9"
    """BTW laag, verkopen 9%"""

    VERL_VERK_L9 = "VERL_VERK_L9"
    """BTW Verlegd 9% (1e op de btw-aangifte)"""

    VERL_VERK = "VERL_VERK"
    """BTW Verlegd 21% (1e op de btw-aangifte)"""

    AFW = "AFW"
    """Afwijkend btw-tarief"""

    BU_EU_VERK = "BU_EU_VERK"
    """Leveringen naar buiten de EU 0%"""

    BI_EU_VERK = "BI_EU_VERK"
    """Goederen naar binnen de EU 0%"""

    BI_EU_VERK_D = "BI_EU_VERK_D"
    """Diensten naar binnen de EU 0%"""

    AFST_VERK = "AFST_VERK"
    """Afstandsverkopen naar binnen de EU 0%"""

    LAAG_INK = "LAAG_INK"
    """
    BTW laag, inkopen

    Indien de boekdatum in 2019 of er na valt, wordt 9% aangehouden, daarvoor 6%.
    """

    LAAG_INK_9 = "LAAG_INK_9"
    """BTW laag, inkopen 9%"""

    VERL_INK_L9 = "VERL_INK_L9"
    """BTW verlegd, laag, inkopen"""

    HOOG_INK = "HOOG_INK"
    """BTW hoog, inkopen"""

    HOOG_INK_21 = "HOOG_INK_21"
    """BTW hoog, inkopen 21%"""

    VERL_INK = "VERL_INK"
    """BTW verlegd, hoog, inkopen"""

    AFW_VERK = "AFW_VERK"
    """Afwijkend btw-tarief verkoop"""

    BU_EU_INK = "BU_EU_INK"
    """Leveringen/diensten van buiten de EU 0%"""

    BI_EU_INK = "BI_EU_INK"
    """Leveringen/diensten van binnen de EU 0%"""

    GEEN = "GEEN"
    """Geen BTW"""
