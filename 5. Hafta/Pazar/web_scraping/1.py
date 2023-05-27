# pip install beautifulSoup4
# pip install requests
# pip install pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL="https://www.icisleri.gov.tr/bilgiteknolojileri"

httpRequest = requests.get(URL)
#print(httpRequest)
#print(httpRequest.headers)
print(httpRequest.text)
html = httpRequest.text
parsedHtml = BeautifulSoup(html, 'html.parser')
print(parsedHtml)