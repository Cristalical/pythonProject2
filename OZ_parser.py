#Парсер 2
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Ozon")
async def OZ_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу "+url)
    headers = {
        'Accept': "*/*",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx GX)"
    }
    soup = soupManager(url, headers)
    if type(soup) is BeautifulSoup:
        pass

