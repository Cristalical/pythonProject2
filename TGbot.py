#Сам ботик
import logging
from aiogram import executor
from create_bot import dp
from keyboard import keyboard

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

dp.register_message_handler(keyboard, commands="start")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)