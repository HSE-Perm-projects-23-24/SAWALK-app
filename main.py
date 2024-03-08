import asyncio
from aiogram import Bot, Dispatcher

# получение роутеров
from users.handlers import user_commands
from admins.handlers import admin_commands

from config_reader import config

admins_chat_id = int(config.admins_chat.get_secret_value())


async def main():
    dp = Dispatcher()
    bot = Bot(config.bot_token.get_secret_value())
    dp.include_routers(
        user_commands.router,
        admin_commands.router
        # bot_messages.router # идет последним, так как обрабатывает все остальные сообщения
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
