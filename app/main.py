"""TODO"""

from litestar import Litestar

from app.database import Base, engine
from .modules.games.controller import game_router
from .modules.purchases.controller import purchase_router


async def init_db() -> None:
    """TODO"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app = Litestar(
    route_handlers=[
        game_router,
        purchase_router,
    ],
    on_startup=[init_db],
)
