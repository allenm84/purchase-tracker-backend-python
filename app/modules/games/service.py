"""TODO"""

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.games.model import Game
from app.modules.games.schema import GameCreateDTO


class GameService:
    """TODO"""

    @staticmethod
    async def create_game(session: AsyncSession, game_create: GameCreateDTO) -> Game:
        """TODO"""
        game = Game(**game_create.model_dump())
        session.add(game)
        await session.commit()
        await session.refresh(game)
        return game

    @staticmethod
    async def list_games(session: AsyncSession) -> list[Game]:
        """TODO"""
        result = await session.execute(select(Game))
        return result.scalars().all()

    @staticmethod
    async def get_game(session: AsyncSession, game_id: int) -> Game | None:
        """TODO"""
        result = await session.execute(select(Game).where(Game.id == game_id))
        return result.scalar_one_or_none()
