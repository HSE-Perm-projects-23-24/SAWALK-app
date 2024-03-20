from aiogram import Router, F
from aiogram.types import Message, ContentType

from filters.chat_type import ChatTypeFilter
from main import admins_chat_id

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(F.photo)
async def photo_msg(message: Message):
    await message.answer("Это точно какое-то изображение!")
    print(message.photo[-1].file_id)
    with open("admins/data_to_delete_by_db/photo_tasks.txt", 'a') as file:
        file.write(message.photo[-1].file_id)

"""@router.message(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):

    start message to group admins or another group

    
    """

