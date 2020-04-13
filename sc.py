

import requests
import json
import os
import time
import sys

from bs4 import BeautifulSoup



url = "https://www.scopus.com/results/authorNamesList.uri?sort=count-f&src=al&sid=4af407f471b74fd2265d3e9327aa307b&sot=al&sdt=al&sl=23&s=AUTHLASTNAME%28Krerowicz%29&st1=Krerowicz&orcidId=&selectionPageSearch=anl&reselectAuthor=false&activeFlag=true&showDocument=false&resultsPerPage=20&offset=1&jtp=false&currentPage=1&previousSelectionCount=0&tooManySelections=false&previousResultCount=0&authSubject=LFSC&authSubject=HLSC&authSubject=PHSC&authSubject=SOSC&exactAuthorSearch=false&showFullList=false&authorPreferredName=&origin=searchauthorfreelookup&affiliationId=&txGid=6a717b5bc045b2e450b8ce7b0293da34"

response = requests.get(url)
#print (response)
soup = BeautifulSoup(response.text, 'lxml').encode("utf-8")
print(soup)



