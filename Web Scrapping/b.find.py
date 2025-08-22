from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

quote = soup.find("span",class_="text")
author = soup.find("small",class_="author")

print(f"Quote : {quote.get_text()}")
print(f"Author : {author.get_text()}")