from aiogram import Router, Bot, F
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from admins.keyboards import inline

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(F.text)
async def variants_settings_menu_handler(message: Message, bot=Bot):
    """
    Функция-обработчик любого текста внутри админ панели
    """
    with open("admins/data_to_delete_by_db/admins_text_changing.txt", 'r') as file:
        admins_text_changing = file.read()

    if admins_text_changing == "None":
        await bot.send_message(
            chat_id=message.chat.id,
            text="Текст пришел, но не был выставлен параметр его определения",
        )
    elif admins_text_changing == "rewrite_name_event":
        await bot.send_message(
            chat_id=message.chat.id,
            text="Текст названия мероприятия пришел и был выставлен",
            reply_markup=inline.to_settings_admins_menu
        )
        with open("admins/data_to_delete_by_db/name_event.txt", 'w') as file:
            file.write(message.text)
        with open("admins/data_to_delete_by_db/admins_text_changing.txt", 'w') as file:
            file.write("None")

