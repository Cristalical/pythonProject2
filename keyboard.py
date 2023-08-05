from aiogram import types
async def keyboard(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="🟣 Wildberries", callback_data="Wildberries"))
    kb.add(types.InlineKeyboardButton(text="🔵 Ozon", callback_data="Ozon"))
    await message.answer("Нажмите для выбора парсинга сайта.", reply_markup=kb)
