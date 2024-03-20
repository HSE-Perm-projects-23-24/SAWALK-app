from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from filters.chat_type import ChatTypeFilter
from admins.keyboards import inline

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


