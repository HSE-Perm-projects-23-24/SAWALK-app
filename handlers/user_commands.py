from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start_bot(message: Message):
    if message.chat.type == "private":
        await message.answer(f"Привет, {message.from_user.first_name}, ghbdftn")
