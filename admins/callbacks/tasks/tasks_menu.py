from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from filters.chat_type import ChatTypeFilter
from admins.keyboards import inline

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.callback_query(lambda callback_query: "change_num_main_tasks_" in callback_query.data)
async def variants_changes_task_admins_menu_handler(callback_query: CallbackQuery, bot=Bot):
    """
    Функция-обработчик изменения определенного основного задания
    """
    await bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )
    await bot.send_message(
        chat_id=callback_query.message.chat.id,
        text=f"Что вы хотели бы изменить в "
             f"{str(callback_query.data).replace("change_num_main_tasks_", "")} задании?",
        reply_markup=inline.variants_changes_main_tasks_menu
    )

