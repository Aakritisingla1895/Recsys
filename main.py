from pprint import pprint
from bs4 import BeautifulSoup
import lxml
import json
import random
import pickle
import string
import requests

base_url = "https://www.longdom.org/advances-in-automobile-engineering/archive.html"
url = "https://www.scitechnol.com/archive-computer-engineering-and-information-technology.php"
try_url = "https://www.omicsonline.org/scholarly automated-reasoning-and-inference-journals-articles-ppts-list.php"

"https://www.omicsonline.org/scholarly/fuzzy-logic-journals-articles-ppts-list.php"
"https://www.ijeast.com/"
"https://www.researchprotocols.org/" --medicine
"http://jea-net.com/vol-7-no-1-june-2019-current-issue-jea"
response = requests.get(try_url)
print(response)


