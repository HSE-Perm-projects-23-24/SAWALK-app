from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from main import admins_chat_id

from filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(CommandStart())
async def start_bot(message: Message):
    """
    start message to group admins or another group
    """
    if message.chat.id == admins_chat_id:
        await message.answer(f"Привет, {message.from_user.first_name}, admin group")
    else:
        await message.answer(f"Привет, {message.from_user.first_name}, group")


