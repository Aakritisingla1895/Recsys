
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import time
import requests
from math import sqrt

title_name = 'A simple dialysis device for large DNA molecules'

try:
    from googlesearch import search
    search_article = str(title_name  + "+futurescience")
    for j in search(search_article, tld="co.in", num=10, stop=1, pause=2):
        result = j
except ImportError:
    print("No module named 'google' found")
# to search

print(result)


response = requests.get(result).text
#print(response)

soup = BeautifulSoup(response, 'lxml').encode("utf-8")
#print(soup)

driver = webdriver.Chrome('E:/Profeza/chromedriver_win32/chromedriver.exe')

driver.get(result)

driver.implicitly_wait(10)


#num_links = len(driver.find_element_by_xpath("//*[@id='pb-page-content']/div/main/article/div/div[1]/div[1]/ul[2]/li/a/@href"))
#print(num_links)

page_source = driver.page_source.encode("utf-8")
#print(page_source)

page = BeautifulSoup(driver.page_source, 'lxml').encode("utf-8")
print(page)
affliations = page.find('div',{'class':'col-sm-12 col-md-8 article__content'})
x = int(sqrt(len(affliations)))
print(x)
time.sleep(1)

driver.close()
