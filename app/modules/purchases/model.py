"""TODO"""

import enum
from sqlalchemy import Column, Integer, ForeignKey, Date, Enum, Numeric
from sqlalchemy.orm import relationship
from app.database import Base


class PurchaseType(enum.Enum):
    """TODO"""

    DEBIT = "Debit"
    CREDIT = "Credit"


class Purchase(Base):
    """TODO"""

    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, nullable=False)
    type = Column(Enum(PurchaseType), nullable=False)

    game = relationship("Game")
