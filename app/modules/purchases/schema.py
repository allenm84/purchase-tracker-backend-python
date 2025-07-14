"""TODO"""

from datetime import date
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel


class PurchaseCreateDTO(BaseModel):
    """TODO"""

    game_id: int
    amount: Decimal
    date: date
    type: Literal["Debit", "Credit"]


class PurchaseDTO(PurchaseCreateDTO):
    """TODO"""

    id: int

    class Config:
        """TODO"""

        from_attributes = True
