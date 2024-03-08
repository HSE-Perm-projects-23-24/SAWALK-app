from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@router.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}, user")
