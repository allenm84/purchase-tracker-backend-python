"""TODO"""

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.purchases.model import Purchase, PurchaseType
from app.modules.purchases.schema import PurchaseCreateDTO


class PurchaseService:
    """TODO"""

    @staticmethod
    async def create_purchase(
        session: AsyncSession, purchase_create: PurchaseCreateDTO
    ) -> Purchase:
        """TODO"""
        purchase = Purchase(
            game_id=purchase_create.game_id,
            amount=purchase_create.amount,
            date=purchase_create.date,
            type=PurchaseType[purchase_create.type],
        )
        session.add(purchase)
        await session.commit()
        await session.refresh(purchase)
        return purchase

    @staticmethod
    async def list_purchases(session: AsyncSession) -> list[Purchase]:
        """TODO"""
        result = await session.execute(select(Purchase))
        return result.scalars().all()
