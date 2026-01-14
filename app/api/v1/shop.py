from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.shop_service import ShopService
from app.repositories.product_repository import ProductRepository

router = APIRouter(prefix="/shop", tags=["shop"])

@router.get("/products")
async def get_products(db: AsyncSession = Depends(get_db)):
    """Получить список товаров для админки"""
    product_repo = ProductRepository(db)
    shop_service = ShopService(product_repo)
    return await shop_service.get_available_products()