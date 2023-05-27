# pip install beautifulSoup4
# pip install requests
# pip install pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL="https://www.icisleri.gov.tr/bilgiteknolojileri"

httpRequest = requests.get(URL)

html = httpRequest.text
parsedHtml = BeautifulSoup(html, 'html.parser')
bolumler= parsedHtml.find_all("div",{"class": "col-lg-3 col-md-4"})
for bolum in bolumler:
    print(bolum.find("h6").get_text())
    print(bolum.find("p").get_text())
    print("-"*30)