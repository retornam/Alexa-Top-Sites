"""
This script downloads the alexa top 1M sites, unzips it, and reads the CSV and
returns a list of the top N sites.
"""

from bs4 import BeautifulSoup
from math import ceil
import requests

ALEXA_DATA_URL = 'http://www.alexa.com/topsites/global'


def top_list(n=500):
    count = 0
    alist = []
    pages = int(ceil(n/25.0))
    for page in range(0, pages):
        response = requests.get(ALEXA_DATA_URL + ";" + str(page))
        soup = BeautifulSoup(response.text, "lxml")
        websites = soup.find_all('li', {'class':'site-listing'})
        for website in websites:
            count = count + 1
            if count > n:
                break
            alist.append((int(website.div.contents[0]), website.a.contents[0].lower()))
        if count > n:
            break
    return alist




if __name__ == "__main__": # pragma: no cover
    print top_list()
