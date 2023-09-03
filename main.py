#requirements
#import requests
#import bs4
#import html5lib

import requests
from bs4 import BeautifulSoup
url="https://timesofindia.indiatimes.com/sports/cricket"

r = requests.get(url)
htmlContent=r.content

# print(htmlContent)

soup=BeautifulSoup(htmlContent,'html.parser')

# print(soup.prettify)

title=soup.title
print(title)