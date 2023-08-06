#Парсер 1
from aiogram import types
from create_bot import dp
from selenium import webdriver
@dp.message_handler(text="Wildberries")
async def WB_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    #headers = {
    #    'Accept': "*/*",
    #    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
    #}
    #res = requests.get(url, headers=headers)
    #with open("txt.json", 'w', encoding="utf-8") as f:
    #    f.write(res.json())
    driver = webdriver.Chrome()
    driver.get(url)
    print(driver.page_source)







