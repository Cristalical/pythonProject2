#Парсер 1
from aiogram import types
from create_bot import dp
@dp.callback_query_handler(text="Wildberries")
async def cmd_test1(call: types.CallbackQuery):
    await call.message.answer("WB_parse")
    await call.answer()
    await call.message.answer(call.message.from_id)


