from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.core.config import settings

# Создаем бота с токеном из настроек
bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)

# Создаем диспетчер с хранилищем в памяти
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
