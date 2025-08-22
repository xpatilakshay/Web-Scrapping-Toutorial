import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

quote = soup.find_all("span",class_="text")
author = soup.find_all("small",class_="author")

for q,a in zip(quote,author):
    print(f"{q.get_text()} - {a.get_text()}")