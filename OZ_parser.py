#Парсер 2
from aiogram import types
from create_bot import dp
@dp.callback_query_handler(text="random_value2")
async def cmd_test2(call: types.CallbackQuery):
    await call.message.answer("OZ_parse")
  #  await message.answer(f'<a href = "tg://user?id={message.from_id}" > Святозар </a> ', parse_mode='HTML')