#Парсер 1
from soup_manager import soupManager
from aiogram import types
from create_bot import dp
@dp.message_handler(text="Wildberries")
async def WB_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    soup = soupManager(url)
    url_new = soup.find('a', class_='pagination-next pagination__next j-next-page')
    with open('txt.txt', "w", encoding='utf-8') as f:
        f.write(str(soup))
    print(url_new)
    try:
        await message.answer(url_new)
    except:
        print('try')







