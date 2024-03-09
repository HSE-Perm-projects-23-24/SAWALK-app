from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_admins_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню➡️", callback_data="admins_menu")
        ]
    ]
)

variants_main_admins_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Задания📝",
                callback_data="tasks_admins_menu"
            )
        ],
        [
            InlineKeyboardButton(
                text="Команды👨🏻‍🤝‍👨🏻👨🏻‍🤝‍👨🏻",
                callback_data="teams_admins_menu"
            )
        ],
        [
            InlineKeyboardButton(
                text="Настройки⚙️",
                callback_data="other_texts_admins_menu"
            )
        ]
    ]
)

variants_tasks_admins_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Основные📝",
                callback_data="main_tasks_admins_menu"
            )
        ],
        [
            InlineKeyboardButton(
                text="Граффити🖼️",
                callback_data="graffiti_tasks_admins_menu"
            )
        ],
        [
            InlineKeyboardButton(
                text="BeReal🐯🦊🐷🐮🐭",
                callback_data="variants_main_admins_menu"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад⬅️",
                callback_data="from_var_tasks_menu_to_admins_mm"
            )
        ]
    ]
)

