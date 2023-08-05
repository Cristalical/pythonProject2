#Парсер 2
from aiogram import types
async def cmd_test2(message: types.Message):
    await message.reply("OZ_parse")
    await message.answer(f'<a href = "tg://user?id={message.from_id}" > Святозар </a> ', parse_mode='HTML')