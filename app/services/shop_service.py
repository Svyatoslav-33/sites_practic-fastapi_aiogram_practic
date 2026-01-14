from app.repositories.product_repository import ProductRepository

class ShopService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo
    
    async def get_available_products(self):
        """Получить только товары в наличии"""
        all_products = await self.product_repo.get_all()
        return [p for p in all_products if p.stock > 0]