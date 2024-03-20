from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup


async def generate_num_main_tasks_to_change(len_main_tasks: str) -> InlineKeyboardMarkup:
    inline_keyboard = []
    for i in range(1, int(len_main_tasks)//2 + 1):
        inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"№ {2*i-1}",
                    callback_data=f'change_num_main_tasks_{2*i-1}'),
                InlineKeyboardButton(
                    text=f"№ {2*i}",
                    callback_data=f'change_num_main_tasks_{2*i}'),
            ]
        )
    if int(len_main_tasks) % 2 == 1:
        inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"№ {len_main_tasks}",
                    callback_data=f'change_num_main_tasks_{len_main_tasks}')
            ]
        )
    inline_keyboard.append([InlineKeyboardButton(
        text=f"Добавить новое задание➕",
        callback_data=f'add_new_main_task')]
    )
    inline_keyboard.append([InlineKeyboardButton(
        text=f"Назад⬅️",
        callback_data=f'tasks_admins_menu')]
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return keyboard
