#Сам ботик
import logging
from aiogram import executor, types
from create_bot import dp
from WB_parser import cmd_test1
from OZ_parser import cmd_test2

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



dp.register_message_handler(cmd_test2, commands="OZ")
dp.register_message_handler(cmd_test1, commands="WB")

@dp.message_handler(commands="start")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="OZ", callback_data="random_value1"))
    keyboard.add(types.InlineKeyboardButton(text="WB", callback_data="random_value2"))
    await message.answer("Нажмите для выбора парсинга сайта.", reply_markup=keyboard)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)