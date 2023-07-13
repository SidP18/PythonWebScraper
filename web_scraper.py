# sends a request to a URL we want to scrape, we will get a response back which will be the data that we require
# need to the requests and beautiful soup python modules
# requests is for sending requests
# beautiful soup is for filtering the data we need specifially

import requests
from bs4 import BeautifulSoup

url_to_scrape = 'https://www.basketball-reference.com/awards/mvp.html'

res = requests.get(url_to_scrape)
print(res)

soup = BeautifulSoup(res.content, 'lxml')
header = soup.find_all('thead')
title = soup.find_all('tbody')

for h in header:
    print(h.getText())


for t in title:
    print(t.getText())


