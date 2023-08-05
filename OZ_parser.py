#Парсер 2
from aiogram import types
from create_bot import dp
@dp.callback_query_handler(text="Ozon")
async def cmd_test2(call: types.CallbackQuery):
    await call.message.answer("OZ_parse")
    await call.answer()