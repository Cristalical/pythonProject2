from bs4 import BeautifulSoup
from selenium import webdriver

def soupManager(url):
    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    return soup



