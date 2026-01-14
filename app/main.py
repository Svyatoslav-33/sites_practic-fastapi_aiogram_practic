"""
Главный файл для запуска FastAPI приложения
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.api.v1 import api_router
from app.bot.loader import dp, bot
from app.database import engine, Base
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Управление жизненным циклом приложения
    - При запуске: создаем таблицы БД, запускаем бота
    - При завершении: останавливаем бота
    """
    logger.info("Запуск приложения...")
    
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Таблицы БД созданы/проверены")
    
  
    import asyncio
    bot_task = asyncio.create_task(dp.start_polling(bot))
    logger.info("Бот запущен в фоновом режиме")
    
    yield  
    
    logger.info("Остановка приложения...")
    bot_task.cancel()
    await bot.close()
    await engine.dispose()
    logger.info("Приложение остановлено")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Telegram Bot Admin Template",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты API
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    """Корневой эндпоинт для проверки работы"""
    return {
        "message": "Telegram Bot Admin Template работает!",
        "docs": "/docs",
        "bot": "Telegram бот запущен и работает",
        "admin": "Админка доступна на /admin",
    }

@app.get("/health")
async def health_check():
    """Эндпоинт для проверки здоровья сервиса"""
    return {"status": "healthy", "service": "telegram-bot-admin"}