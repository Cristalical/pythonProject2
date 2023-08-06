#Парсер 1
from soup_manager import soupManager
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Wildberries")
async def WB_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    soup = soupManager(url)
    url_new = soup.find('a', class_='pagination')
    print(url_new)
    await message.answer(url_new)







