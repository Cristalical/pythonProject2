#Парсер 2
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Ozon")
async def OZ_parse(message: types.Message, url):
    await message.answer("OZ_parse "+url)
