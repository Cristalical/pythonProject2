#Сам ботик
import logging
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token="6420484725:AAHU-UQ2oylCgjR_wTiiTsseB-lYQS6g1js")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)