#Парсер 1
from aiogram import types
from create_bot import dp
@dp.callback_query_handler(text="Wildberries")
async def WB_parse(message: types.Message, url='sd'):
    await message.answer("WB_parse ", url)



