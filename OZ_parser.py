#Парсер 2
from soup_manager import soupManager
from aiogram import types
from create_bot import dp
from Saving import save
@dp.message_handler(text="Ozon")
async def OZ_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    url = url
    i = 2
    def parsing(url, i):
        soup = soupManager(url)
        url_new = 'https://www.ozon.ru' + soup.find('a', class_='a2-a4').get('href')
        cells = soup.find_all('div', class_='i9j ik')

        for cell in cells:
            name = cell.find('span', class_='tsBody500Medium').text
            price = cell.find('span', class_='c3-a1 tsHeadline500Medium c3-b9').text
            try:
                rating = cell.find('svg', class_='du4').findNext('span').text
            except:
                rating = "Нет оценки"
            link = 'https://www.ozon.ru' + cell.find('a', class_='tile-hover-target yh3 h4y').get('href')
            save(name, price, rating, link, i)

        return url_new
    while url:
        url = parsing(url, i)
        i += 1
        print(url)



