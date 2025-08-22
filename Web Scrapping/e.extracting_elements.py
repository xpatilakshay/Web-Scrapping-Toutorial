import requests
from bs4 import BeautifulSoup


url="http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# for link in soup.find_all("a",href=True,title=True): #here it is not running because both href and title need to be there in anchor but there us no element with anchor so ie won't run
#     print(f"{link['href']} || {link['title']}")

# links = soup.find_all("a")
# for link in links[:5]: #for first 5 anchors
#     print(f"Text : {link.get_text()} || HREF : {link['href']}")

# imgs = soup.find_all("img")
# for img in imgs[:5]:
#     print(f"Image Source {img['src']}")
#     print(f"Image Alt : {img['alt']}")


# Navigating the HTML Tree (Parent, Child, Sibling)

quote_div = soup.find("div",class_="quote")

quote_text = quote_div.find("span",class_="text").get_text()
author = quote_div.find("small",class_="author").get_text()

print(f"{quote_text} - {author}")

print("Parent tag : ",quote_div.parent.name)
print("Next Sibling : ",quote_div.next_sibling)


# Select all quote texts using CSS
quotes = soup.select("div.quote span.text")
authors = soup.select("div.quote small.author")

for q,a in zip(quotes[:3],authors[:3]):
    print(q.get_text()," - ",a.get_text())

#Another way to do same thing as above

quote_divs = soup.select("div.quote")

for div in quote_divs[:3]:
    q = div.select_one("span.text").get_text()
    a = div.select_one("small.author").get_text()
    print(q," - ",a)

# Handling Ids and Classes
print(soup.find(id="main-content").get_text())
print(soup.find(class_="content").get_text())

