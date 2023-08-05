#Парсер 1
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Wildberries")
async def WB_parse(message: types.Message, url):
    await message.answer("WB_parse "+url)



