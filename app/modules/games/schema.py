"""TODO"""

from datetime import date
from pydantic import BaseModel


class GameCreateDTO(BaseModel):
    """TODO"""

    name: str
    release_date: date


class GameDTO(GameCreateDTO):
    """TODO"""

    id: int

    class Config:
        """TODO"""

        from_attributes = True
