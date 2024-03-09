from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter

from working_with_time import get_my_time
from data.variables import name_event
from users.keyboards import inline


router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@router.message(CommandStart())
async def start_bot(message: Message):
    """
    start message to users of this bot
    """
    await message.answer(
        text=f"{await get_my_time.get_greeting()}, добро пожаловать на\n{name_event}. 👋\n\n"
        f"Это бот создан для отправки ответов на загадки и дополнительные задания. "
        f"Вы можете изучить инструкции, войти в свой аккаунт и начать использовать бота",
        reply_markup=inline.terms_use
    )
