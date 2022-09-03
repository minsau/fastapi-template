import logging
from decimal import Decimal, InvalidOperation
from re import sub
from typing import Union

logger = logging.getLogger(__name__)


def currency_to_decimal(currency: Union[str, float]) -> Decimal:
    try:
        if type(currency) == str:
            currency = sub(r"[^\d.]", "", currency)
            return Decimal(currency)
        return Decimal(currency)
    except (InvalidOperation, TypeError) as e:
        logger.warning(
            f"currency could not be converted to decimal {currency}, type: {type(currency)},"
            f" error: {e}"
        )
        return Decimal(0)
