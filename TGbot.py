#Сам ботик
import logging
from aiogram import executor
from create_bot import dp
from WB_parser import cmd_test1 #ИСПОЛЬЗУЕТСЯ!!!
from OZ_parser import cmd_test2 #ИСПОЛЬЗУЕТСЯ!!!
from keyboard import keyboard

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


dp.register_message_handler(keyboard, commands="start")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)