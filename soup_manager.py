import requests
from bs4 import BeautifulSoup
def soupManager(url, headers):
    res = requests.get(url, headers=headers)
    if res:
        res.encoding = 'windows-1251'
        return BeautifulSoup(res.text, 'lxml')
    else:
        print(f"Error: {res.status_code}")
        return False