import logging

from aiogram import Dispatcher

from data.config import ADMINS
# from states.languages import Language


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            msg = f"🇺🇿 Bot ishga tushdi!"\
                    f"🇬🇧 Bot started!"\
                    f"🇷🇺 Бот запущен!"
            
            await dp.bot.send_message(admin, msg)

        except Exception as err:
            logging.exception(err)
