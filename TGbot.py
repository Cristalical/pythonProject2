#Сам ботик
import logging
from aiogram import executor, types
from create_bot import dp, bot_name
from WB_parser import WB_parse
from OZ_parser import OZ_parse
from keyboard import keyboard

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


#функция выбора парсера по второму слову в списке полученных слов пользователя
async def filters(message: types.Message):
    msgs = message.text.split()
    if msgs[0] == bot_name:
        msgs.pop(0)
        shop = msgs.pop(0)
        if shop == 'Wildberries':
            url = 'https://www.wildberries.ru/catalog/0/search.aspx?search=' + '%20'.join(msgs)
            await WB_parse(message, url=url)
        elif shop == 'Ozon':
            url = f"https://www.ozon.ru/search/?text={'+'.join(msgs)}&from_global=true"
            await OZ_parse(message, url=url)


dp.register_message_handler(keyboard, commands="start")
dp.register_message_handler(filters)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)