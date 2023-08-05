from aiogram import types
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="🟣 Wildberries", callback_data="random_value1"))
    keyboard.add(types.InlineKeyboardButton(text="🔵 Ozon", callback_data="random_value2"))
    await message.answer("Нажмите для выбора парсинга сайта.", reply_markup=keyboard)
