#Парсер 2
from bs4 import BeautifulSoup
from selenium import webdriver
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Ozon")
async def OZ_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source)
    url_new = soup.find('a', class_='a2-a4').get('href')
    print(url_new)










    headers = {
        'Accept': "application/json",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx 05)"
    }

