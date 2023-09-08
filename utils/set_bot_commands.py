from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🔁 Botni ishga tushurish/Запустить бота/Start the bot"),
            types.BotCommand("help", "❔ Yordam/Помощь/Help"),
        ]
    )
