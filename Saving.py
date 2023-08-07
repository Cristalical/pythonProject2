import openpyxl as op
def save(name, price, rating, link, i):
    #имя файла
    filename = 'OZ.xlsx'
    #создание Workbook
    wb = op.Workbook()
    sheet = wb.active
    #Вводим таблицы
    c = sheet.cell(row = 1, column = 1)
    c1 = sheet.cell(row = 1, column = 2)
    c2 = sheet.cell(row = 1, column = 3)
    c3 = sheet.cell(row = 1, column = 4)
    c4 = sheet.cell(row = 1, column = 5)
    #Вводим данные таблицы
    c.value = "№"
    c1.value = "Название"
    c2.value = "Цена"
    c3.value = "Рейтинг"
    c4.value = "Ссылка"
    #Сохраняем файл
    c = sheet.cell(row=i, column=1)
    c1 = sheet.cell(row=i, column=2)
    c2 = sheet.cell(row=i, column=3)
    c3 = sheet.cell(row=i, column=4)
    c4 = sheet.cell(row=i, column=5)
    c.value = i-1
    c1.value = name
    c2.value = price
    c3.value = rating
    c4.value = link
    i += 1
    wb.save(filename)