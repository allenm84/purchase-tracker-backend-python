"""TODO"""

from litestar import Controller, get, post, Router
from app.modules.games.service import GameService
from app.modules.games.schema import GameCreateDTO, GameDTO
from app.database import SessionLocal


class GameController(Controller):
    """TODO"""

    @get("/", response_model=list[GameDTO])
    async def list_games(self) -> list[GameDTO]:
        """TODO"""
        async with SessionLocal() as session:
            games = await GameService.list_games(session)
            return [GameDTO.model_validate(game) for game in games]

    @post("/", response_model=GameDTO)
    async def create_game(self, data: GameCreateDTO) -> GameDTO:
        """TODO"""
        async with SessionLocal() as session:
            game = await GameService.create_game(session, data)
            return GameDTO.model_validate(game)


game_router = Router(path="/games", route_handlers=[GameController])
