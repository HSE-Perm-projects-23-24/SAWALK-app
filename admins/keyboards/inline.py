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
                callback_data="settings_admins_menu"
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
                callback_data="to_admins_mm"
            )
        ]
    ]
)

variants_changes_main_tasks_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Текст",
                callback_data="change_text_one_of_main_tasks"
            )
        ],
        [
            InlineKeyboardButton(
                text="Фото",
                callback_data="change_photo_one_of_main_tasks"
            )
        ],
        [
            InlineKeyboardButton(
                text="Баллы",
                callback_data="change_points_one_of_main_tasks"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад⬅️",
                callback_data="main_tasks_admins_menu"
            )
        ]
    ]
)
