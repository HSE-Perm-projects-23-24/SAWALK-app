from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from admins.keyboards import inline
from working_with_time import get_my_time


router = Router()


@router.callback_query(lambda callback_query: callback_query.data == "admins_menu")
async def variants_rules_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик кнопки стартового сообщения для администраторов
    """
    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )
    await bot.edit_message_text(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        text=f"{await get_my_time.get_greeting()}, admin group."
    )
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="Основное меню выбора",
        reply_markup=inline.variants_main_admins_menu
    )


@router.callback_query(
    lambda callback_query: callback_query.data in ["tasks_admins_menu", "teams_admins_menu", "other_texts_admins_menu"])
async def rules_photos_and_message_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик варианта из основного меню администраторов
    """
    if callback_query.data == "tasks_admins_menu":
        await bot.delete_message(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id
        )
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Меню изменения конкретных заданий",
            reply_markup=inline.variants_tasks_admins_menu
        )
    elif callback_query.data == "teams_admins_menu":
        pass
    elif callback_query.data == "other_texts_admins_menu":
        pass


@router.callback_query(lambda callback_query: callback_query.data == "from_var_tasks_menu_to_admins_mm")
async def variants_rules_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик кнопки назад от меню с изменениями
    """
    await bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text="Основное меню выбора",
        reply_markup=inline.variants_main_admins_menu
    )




