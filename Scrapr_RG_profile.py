import json
import os
import requests
from bs4 import BeautifulSoup as BS
from googlesearch import search
from pprint import pprint

import os
#from getJSExecutedHTML import getJSExecutedHTML



author_url_1 = 'https://www.researchgate.net/profile/Gilles_Malherbe'
author_url_2 = 'https://www.researchgate.net/profile/David_Humphreys10'
author_url_3 = 'https://www.researchgate.net/profile/Emma_Dave'

article_url = 'https://www.researchgate.net/publication/332449458_A_robust_fractionation_method_for_protein_subcellular_localization_studies_in_Escherichia_coli'



try:
    from googlesearch import search

except ImportError:
    print("No module named 'google' found")
    # to search
for j in search(author_url_1, tld="co.in", num=10, stop=1, pause=2):
    result = j
    print(j)
    


def scrape_author_details(author_url_1):
    i=1
    while i>0:
        if i<=100:
            try:
                proxies = {'http': 'http://10.10.1.10:3128'}
                response = requests.get(result, proxies=proxies,timeout=10)
                
            except:
               
                continue
            else:
                print("under 50 count, website is blocking our proxy.")
                break
            if len(response) <= 0:
                    continue
            try:
                soup = BS(response, 'lxml')
                article_title = soup.find_all('h1', {'class' : "publication-details__title"})[0].text.strip()
                break
            except Exception:
                continue
            break
        soup = BS(response.text, 'lxml').encode("utf-8")
        article_title = soup.find('h1', {'class' : "publication-details__title"})[0].text.strip()
        print (article_title)
    
print (scrape_author_details(author_url_1))