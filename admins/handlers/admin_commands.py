from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from main import admins_chat_id
from working_with_time import get_my_time
from admins.keyboards import inline

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
        await message.answer(
            text=f"{await get_my_time.get_greeting()}, admin group.\n\n"
                 f"Вы можете перейти в основное меню",
            reply_markup=inline.start_admins_menu
        )
    else:
        await message.answer(
            f"Привет, {message.from_user.first_name}, group.\n\n"
            f"Вы пока ничего делать не можете, но скоро сможете"
        )


