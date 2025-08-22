# import requests
# from bs4 import BeautifulSoup

# all_quotes = []
# page = 1

# while True:
#     url = f"http://quotes.toscrape.com/page/{page}/"
#     response = requests.get(url)

#     if response.status_code!=200:
#         break

#     soup = BeautifulSoup(response.text,"html.parser")

#     quotes = soup.find_all("span",class_="text")
#     author = soup.find_all("small",class_="author")

#     if not quotes:
#         break

#     for q,a in zip(quotes,author):
#         all_quotes.append({"Quote":q.get_text(),"Author":a.get_text()})

#     print(f"Page {page} Scapped successfully!...")
#     page+=1

# print(f"Total Quotes Scrapped : {len(all_quotes)}")
# print(all_quotes)



# Explanation of Keywords:

# while True: → starts an infinite loop. We’ll break when there are no more pages.

# f"http://quotes.toscrape.com/page/{page}/" → f-string (formatted string) to insert page number into URL.

# if response.status_code != 200: → stop if page doesn’t exist.

# soup.find_all(...) → extract all elements on that page.

# if not quotes: → if no quotes found → last page reached.

# all_quotes.append({...}) → add dictionary of quote+author to list.

# page += 1 → move to next page.




import requests
from bs4 import BeautifulSoup

all_quotes = []
page = 1

while True:
    url = f"http://quotes.toscrape.com/page/{page}"
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text,"html.parser")

    quotes = soup.find_all("span",class_="text")
    author = soup.find_all("small",class_="author")

    if not quotes:
        break

    for q,a in zip(quotes,author):
        all_quotes.append({"Quote":q.get_text(),"Author":a.get_text()})

    print(f"page {page} Scrapped Successfully!..")
    print(f"{len(all_quotes)} Quotes found till now...")
    page+=1

print(f"Total Number of quotes are {len(all_quotes)}")
for item in all_quotes:
    print(item["Quote"], "-", item["Author"])




import pandas as pd

df = pd.DataFrame(all_quotes)

df.to_csv("quotes.csv",index=False)
print("file successfully loaded with data..")
print(df.head())

