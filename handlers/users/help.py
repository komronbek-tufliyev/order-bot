from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
#     uz/ru/en
    text = ("Buyruqlar/ Команды/ Commands: ",
            "/start -🔁 Botni ishga tushirish/ Запустить бота/ Start the bot",
            "/help - ❔ Yordam/ Помощь/ Help",)
    
    await message.answer("\n".join(text))
