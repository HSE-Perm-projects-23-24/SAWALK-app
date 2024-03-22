from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from filters.chat_type import ChatTypeFilter
from admins.keyboards import inline, inline_builders
from working_with_time import get_my_time

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)

with open("admins/data_to_delete_by_db/len_main_tasks.txt", 'r') as file:
    len_main_tasks = file.read()


@router.callback_query(lambda callback_query: callback_query.data == "admins_menu")
async def main_admins_menu_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Основное меню администраторов
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
        text="Основное меню",
        reply_markup=inline.variants_main_admins_menu
    )


@router.callback_query(
    lambda callback_query: callback_query.data in
                           [
                               "tasks_admins_menu",
                               "teams_admins_menu",
                               "settings_admins_menu"
                           ])
async def variants_main_admins_menu_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик варианта из основного меню администраторов
    """
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id
                             )

    if callback_query.data == "tasks_admins_menu":
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Меню изменения конкретных заданий",
            reply_markup=inline.variants_tasks_admins_menu
        )
    elif callback_query.data == "teams_admins_menu":
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Тут будет работа с командами для авторизации"
        )
    elif callback_query.data == "settings_admins_menu":
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Что вы хотели бы изменить",
            reply_markup=inline.variants_settings_menu
        )


@router.callback_query(
    lambda callback_query: callback_query.data in
                           [
                               "main_tasks_admins_menu",
                               "graffiti_tasks_admins_menu",
                               "variants_main_admins_menu"
                           ])
async def variants_tasks_admins_menu_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик различных вариантов из заданий
    """
    await bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )

    if callback_query.data == "main_tasks_admins_menu":
        reply_markup = await inline_builders.generate_num_main_tasks_to_change(len_main_tasks)
        await bot.send_message(
            chat_id=callback_query.message.chat.id,
            text="Выберите задание, с которым хотите взаимодействовать",
            reply_markup=reply_markup
        )
    elif callback_query.data == "graffiti_tasks_admins_menu":
        pass
    elif callback_query.data == "variants_main_admins_menu":
        pass


@router.callback_query(lambda callback_query: callback_query.data == "to_admins_mm")
async def variants_rules_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик, переходящий в основное меню админов
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


