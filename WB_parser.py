#Парсер 1
from bs4 import BeautifulSoup
from soup_manager import soupManager
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Wildberries")
async def WB_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    headers = {
        'Accept': "*/*",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition Yx GX)"
    }
    soup = soupManager(url, headers)
    if type(soup) is BeautifulSoup:
        pass







