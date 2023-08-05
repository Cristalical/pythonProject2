#Сам ботик
import logging
from aiogram import executor, types
from create_bot import dp
from WB_parser import cmd_test1
from OZ_parser import cmd_test2
from keyboard import cmd_random

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

dp.register_message_handler(cmd_test2, commands="Ozon")
dp.register_message_handler(cmd_test1, commands="Wildberries")
dp.register_message_handler(cmd_random, commands="start")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)