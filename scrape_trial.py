import requests
import json
import os
import time
import sys
from googlesearch import search

from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?user=35owm6EAAAAJ&hl=en"



response = requests.get(url)
#print (response)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)


author = soup.find_all('div', {'id' : "gsc_prf_i"})
for author_affliation in soup.find('div', {'class' : "gsc_prf_il"}):
    print(author_affliation)

#print(author)

