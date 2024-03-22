from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

terms_use = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Правила пользования📋", callback_data="variants_rules")
        ]
    ]
)

variants_terms_use = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Фото📷",
                callback_data="rules_photos"
            ),
            InlineKeyboardButton(
                text="Сообщение✉️",
                callback_data="rules_message"
            )
        ]
    ]
)

to_authorization = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Вход в аккаунт",
                callback_data="go_to_authorization"
            )
        ]
    ]
)
