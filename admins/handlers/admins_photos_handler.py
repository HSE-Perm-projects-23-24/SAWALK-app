from aiogram import Router, Bot, F
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from admins.keyboards import inline

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(F.photo)
async def photo_msg(message: Message, bot=Bot):
    """
    Функция-обработчик любого текста внутри админ панели
    """
    with open("admins/data_to_delete_by_db/admins_photos_changing.txt", 'r') as file:
        admins_photos_changing = file.read()

    if admins_photos_changing == "None":
        await bot.send_message(
            chat_id=message.chat.id,
            text="Фото пришло, но не был выставлен параметр его определения",
        )
    elif admins_photos_changing == "photo_FAQ":
        await bot.send_message(
            chat_id=message.chat.id,
            text="Фотография FAQ пришла и была выставлена",
            reply_markup=inline.to_settings_admins_menu
        )
        print(message.photo[-1].file_id)
        with open("admins/data_to_delete_by_db/FAQ_photo.txt", 'w') as file:
            file.write(message.photo[-1].file_id)
        with open("admins/data_to_delete_by_db/admins_photos_changing.txt", 'w') as file:
            file.write("None")


