#Парсер 2
from soup_manager import soupManager
from aiogram import types
from create_bot import dp
from Saving import save
@dp.message_handler(text="Ozon")
async def OZ_parse(message: types.Message, url):
    await message.answer("Начинается парсинг по запросу ⬇️\n"+url)
    # Переменная для сохранения данных в таблицу, используется для создания строк и
    # нумерации полученных данных в файле Saving.py
    i = 2
    # Основная функция для парсинга данных
    def parsing(url, i):
        soup = soupManager(url)

        # Исключение, созданное для окончания работы парсера с помощью выхода из цикла
        try:
        # Ссылка на следующую страницу с товарами
            url_new = 'https://www.ozon.ru' + soup.find('a', class_='a2-a4').get('href')
        except:
            url_new = False
        # Данные со всех ячеек товаров, сохранённые в список
        cells = soup.find_all('div', class_='i9j ik')
        # Цикл для перебора каждой ячейки из списка
        for cell in cells:
            # Получение имени товара
            name = cell.find('span', class_='tsBody500Medium').text
            # Получение цены товара
            price = cell.find('span', class_='c3-a1 tsHeadline500Medium c3-b9').text
            # Исключение для обхода ошибки, которая появляется из-за отсутствия рейтинга у некоторых товаров
            try:
                # Получение рейтинга товара
                rating = cell.find('svg', class_='du4').findNext('span').text
            except:
                rating = "Нет оценки"
            # Получение ссылки на товар
            link = 'https://www.ozon.ru' + cell.find('a', class_='tile-hover-target yh3 h4y').get('href')
            # Вызов функции для сохранения данных в Excel
            save(name, price, rating, link, i)
        # Функция возвращает URL следующей страницы с товарами
        return url_new
    while url:
        # Вызов функции парсинга и присвоение переменной нового URL
        url = parsing(url, i)
        # Увеличение значения переменной для занесения данных в следующую строку в Excel
        i += 1
        # Вывод нового URL в чат телеграмм для видимости работы парсера
        await message.answer("ХОП")
