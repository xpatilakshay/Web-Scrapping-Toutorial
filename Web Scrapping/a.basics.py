# Importing required libraries
import requests

# url through which to scrap
url = "http://quotes.toscrape.com/"
response = requests.get(url)

print(response.status_code)
print(response.text[:500])



# Explanation of Keywords:

# import requests → load the library.

# url → website address.

# requests.get(url) → sends a GET request (most common type).

# response → object returned by server.

# response.status_code → tells if request succeeded (200 = success, 404 = not found, 500 = server error).

# response.text → the raw HTML content.
