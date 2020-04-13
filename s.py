import time
from selenium import webdriver
from bs4 import BeautifulSoup


# Create a new Firefox browser object
browser = webdriver.Chrome('E:/Profeza/chromedriver_win32/chromedriver.exe')

try:
    # Go to a website, click the element with the id 'show-data' and wait 2 secs
    browser.get('https://www.scitechnol.com/ArchiveJCEIT/jceit-archive.php?month=September&year=2018&journal=JCEIT')
    browser.find_element_by_id('show_stats').click()
    time.sleep(2)

    # Create BeautifulSoup object from page source.
    page = BeautifulSoup(browser.page_source, 'html.parser')

    # Parse and extract the data that you need.
    rows = page.select('table#stats tbody tr')
    data = {}
    for row in rows:
        tds = row.select('td')
        if tds:
            data[tds[0].text] = tds[1].text
except Exception as e:
    print(e)
finally:
    browser.quit()