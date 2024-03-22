from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from filters.chat_type import ChatTypeFilter
from admins.keyboards import inline

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.callback_query(
    lambda callback_query: callback_query.data in
                           [
                               "texts_settings",
                               "photos_settings"
                           ])
async def variants_settings_menu_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик различных вариантов настроек
    """
    await bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )

    if callback_query.data == "texts_settings":
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Выберите текст для изменения",
            reply_markup=inline.texts_settings_menu
        )
    elif callback_query.data == "photos_settings":
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Выберите фотографии для изменения",
            reply_markup=inline.photos_settings_menu
        )


@router.callback_query(lambda callback_query: callback_query.data in ["name_event_settings"])
async def rewrite_any_texts_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Обработчик вариантов изменения текстов
    """
    if callback_query.data == "name_event_settings":
        await bot.delete_message(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id
        )

        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Вы можете написать новое название мероприятия"
        )

        with open("admins/data_to_delete_by_db/admins_text_changing.txt", 'w') as file:
            file.write("rewrite_name_event")


@router.callback_query(lambda callback_query: callback_query.data in ["faq_photo_settings"])
async def photo_any_photos_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Обработчик вариантов изменения фотографий
    """
    if callback_query.data == "faq_photo_settings":
        await bot.delete_message(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id
        )

        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Вы можете Отправить одно фото-новое FAQ для пользователей"
        )

        with open("admins/data_to_delete_by_db/admins_photos_changing.txt", 'w') as file:
            file.write("photo_FAQ")


