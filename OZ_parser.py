#Парсер 2
from soup_manager import soupManager
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Ozon")
async def OZ_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    soup = soupManager(url)
    url_new = 'https://www.ozon.ru' + soup.find('a', class_='a2-a4').get('href')
    print(url_new)
    await message.answer("страница 2: ⬇️\n" + url_new)

