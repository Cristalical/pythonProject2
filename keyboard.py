from aiogram import types
async def keyboard(message: types.Message):

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(
    text="🟣 Wildberries",
    switch_inline_query_current_chat="Wildberries "))
    kb.add(types.InlineKeyboardButton(text="🔵 Ozon", switch_inline_query_current_chat="Ozon "))
    await message.answer("Нажмите для выбора парсинга сайта.", reply_markup=kb)
#dff