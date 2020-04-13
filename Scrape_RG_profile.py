import re
import requests
import json
from pprint import pprint
import random
from bs4 import BeautifulSoup
from googlesearch import search
from lxml import html
import uuid
import traceback
import pandas
import sysconfig
import os
import sys


agent = {'User-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
def getIP():
    with open("IP.txt") as f:
        host = f.read().strip()
        if not host.index(':'):
            host += ':5000'
    return host

def fetch_article_list():
    host = getIP()

    r = requests.get("Subcellular Fractionation of Hela Cells for Lysosome Enrichment  Using a Continuous Percoll-density Gradient" + "research gate" + host, headers=agent)
    links = []
    soup = BeautifulSoup(r.text, "lxml")
    print (soup)


