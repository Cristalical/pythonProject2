import pandas as pd
import requests
def res():
    search = input()
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BD%D0%BE%D1%81%D0%BA%D0%B8&ssubject=4',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    headers.update({'Referer': f'https://www.wildberries.ru/catalog/0/search.aspx?search={search}&ssubject=4'})

    response = requests.get(
        f'https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=no_test&TestID=no_test&appType=1&curr=rub&dest=-1257786&query={search}&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&resultset=filters&spp=0&subject=4&suppressSpellcheck=false',
        headers=headers,
    )
    return response.json

#with open('txt.txt', 'w') as f:
#    f.write(res())

#def prepare_items(response):
#    products=[]
#    products_raw = response.get('data', {}).get('products', None)
#    if products_raw != None and len(products_raw) > 0:
#        for product in products_raw:
#            products.append({})