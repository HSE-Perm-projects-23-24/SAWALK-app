from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from users.keyboards import inline

router = Router()


@router.callback_query(lambda callback_query: callback_query.data == "start_authorization")
async def start_authorization(callback_query: CallbackQuery, bot=Bot):
    """
    Функция, отвечающая на сообщение с выбором варианта представления FAQ
    """
    with open("admins/data_to_delete_by_db/FAQ_photo.txt", 'r') as file:
        photo_tg_id = file.read()
    if callback_query.data == "rules_photos":
        await bot.send_photo(
            chat_id=callback_query.message.chat.id,
            photo=photo_tg_id,
            caption="Привет!",
            reply_markup=inline.to_authorization
        )
    elif callback_query.data == "rules_message":
        print("присылаем сообщение правил")
