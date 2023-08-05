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
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

    from aiogram.dispatcher.filters import Text
    @dp.message_handler(Text(equals="С пюрешкой"))
    async def with_puree(message: types.Message):
        await message.reply("Отличный выбор!")

    @dp.message_handler(lambda message: message.text == "Без пюрешки")
    async def without_puree(message: types.Message):
        await message.reply("Так невкусно!")
dp.register_message_handler(cmd_start, commands="STR")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)