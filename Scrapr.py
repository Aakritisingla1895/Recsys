import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
import json
import pickle
import os

import selenium
from selenium import webdriver
import time

url = "https://www.scitechnol.com/archive-computer-engineering-and-information-technology.php"

links_list_file = "links_list.dat"


driver = webdriver.Chrome('E:/Profeza/chromedriver_win32/chromedriver.exe')

response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

title = soup.find_all('div', {'class' : "divider-v4 divider-v4-left-double blog-grid-content"})
#print (title)

article_title = soup.find_all('h3', {'class' : "color-base"})
#print (article_title)

links = soup.find('ul',{'class': "list-inline"} )
#print (links)

def get_links():

    list_of_links = []
    for ul in title:
        for li in ul.find_all('li'):
            if li.find('ul'):
                break
            list_of_links.append(li)

    return list_of_links


    

    #print (list_of_links)   


#print (get_links())


def automate_scrape_data():

    driver.get("https://www.scitechnol.com/ArchiveJCEIT/jceit-archive.php?month=April&amp;year=2017&amp;journal=JCEIT")
    more_buttons = driver.find_elements_by_class_name("news-v1-heading-title")
    time.sleep(1)
    page_source = driver.page_source
    #print(page_source)

    soup = BeautifulSoup(page_source, 'lxml')
    data = soup.find_all('div', {'class': 'news-v1-heading'})
    for x in data:
         article_title = data.find_all('h3', {'class': 'news-v1-heading-title'})('a').text.strip()
         print(article_title)
    


  
    driver.close()

    return True
print(automate_scrape_data())
