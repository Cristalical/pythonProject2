#Парсер 1
from aiogram import types
async def cmd_test1(message: types.Message):
    await message.reply("WB_parse")
    await message.reply(message.from_user.username)