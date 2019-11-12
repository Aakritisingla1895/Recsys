import selenium

from selenium import webdriver
import os
import pprint
import time

from bs4 import BeautifulSoup



driver = webdriver.Chrome('E:/Profeza/chromedriver_win32/chromedriver.exe')

    
driver.get("https://www.scitechnol.com/ArchiveJCEIT/jceit-archive.php?month=September&year=2018&journal=JCEIT")
more_buttons = driver.find_elements_by_class_name("news-v1")
#driver.execute_script("arguments[0].click();")
time.sleep(2)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'lxml')
data = driver.find_elements_by_class_name("news-v1-heading")
time.sleep(1)

print (data)

driver.close()

