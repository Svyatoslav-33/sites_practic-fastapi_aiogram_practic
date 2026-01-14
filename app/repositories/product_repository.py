from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession 
from app.models.product import Product 

class ProductRepository:
  def __init__(self, session: AsyncSession):
    self.session = session 

    async def get_all(self):
        result = await self.session.execute(select(Product))
        return result.scalars().all()
    
    async def get_by_id(self, product_id: int):
        result = await self.session.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()