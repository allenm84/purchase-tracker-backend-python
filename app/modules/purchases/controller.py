"""TODO"""

from litestar import Controller, get, post, Router
from app.modules.purchases.schema import PurchaseCreateDTO, PurchaseDTO
from app.modules.purchases.service import PurchaseService
from app.database import SessionLocal


class PurchaseController(Controller):
    """TODO"""

    @get("/", response_model=list[PurchaseDTO])
    async def list_purchases(self) -> list[PurchaseDTO]:
        """TODO"""
        async with SessionLocal() as session:
            purchases = await PurchaseService.list_purchases(session)
            return [PurchaseDTO.model_validate(p) for p in purchases]

    @post("/", response_model=PurchaseDTO)
    async def create_purchase(self, data: PurchaseCreateDTO) -> PurchaseDTO:
        """TODO"""
        async with SessionLocal() as session:
            purchase = await PurchaseService.create_purchase(session, data)
            return PurchaseDTO.model_validate(purchase)


purchase_router = Router(path="/purchases", route_handlers=[PurchaseController])
