# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# chrome_driver_path = "/home/silk2023/Downloads/akshay/cdriver/chromedriver-linux64/chromedriver"
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# driver.get("https://quotes.toscrape.com/js")

# driver.quit()  


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Explanation:

# from selenium import webdriver

# Imports the Selenium WebDriver module which lets Python control a browser.

# from selenium.webdriver.chrome.service import Service

# In Selenium v4+, ChromeDriver must be wrapped in a Service object.

# This handles starting and stopping the Chrome browser process.

# from selenium.webdriver.common.by import By

# By is used to specify how to locate elements (by ID, class, CSS, XPath, etc.).

# from selenium.webdriver.support.ui import WebDriverWait

# WebDriverWait allows us to wait until elements load on the page.

# Essential for dynamic JS pages that load content asynchronously.

# from selenium.webdriver.support import expected_conditions as EC

# expected_conditions contains predefined conditions for waits, like:

# presence_of_element_located → wait until an element is present.

# visibility_of_element_located → wait until element is visible.


chrome_driver_path = "/home/silk2023/Downloads/akshay/cdriver/chromedriver-linux64/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Explanation:

# chrome_driver_path = ".../chromedriver"

# This is the full path to your ChromeDriver executable.

# ChromeDriver is what Selenium uses to control Chrome.

# service = Service(executable_path=chrome_driver_path)

# Wraps the driver in a Service object, required in Selenium v4+.

# Ensures proper startup and shutdown of Chrome.

# driver = webdriver.Chrome(service=service)

# Creates a Chrome browser instance controlled by Selenium.

# driver is now your handle to control the browser (open pages, click buttons, extract text).

driver.get("https://quotes.toscrape.com/js")

'''
Explanation:

Opens the given URL in Chrome.

Equivalent to typing the URL in the browser and pressing Enter.

At this point, the browser is visible and the page starts loading.

'''

wait = WebDriverWait(driver, 10)
quote_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))


'''
Explanation:

wait = WebDriverWait(driver, 10)

Creates a wait object that can pause the code for up to 10 seconds while waiting for something to appear.

quote_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

Waits until at least one element with class quote appears on the page.

EC.presence_of_element_located → condition that checks if the element exists in the DOM.

By.CLASS_NAME, "quote" → tells Selenium to look for elements by class name.

Returns the first element found.

✅ This is important for JS pages because the content may load asynchronously, so we can’t scrape immediately after get().
'''

text = quote_element.find_element(By.CLASS_NAME, "text").text
author = quote_element.find_element(By.CLASS_NAME, "author").text   

'''Explanation:

quote_element.find_element(By.CLASS_NAME, "text")

Finds the child element inside the quote element with class text (the actual quote text).

.text

Extracts only the visible text inside that tag (ignores HTML tags).

Similarly, quote_element.find_element(By.CLASS_NAME, "author").text

Finds the author of that quote and extracts its text.'''

print(f"{text} - {author}")

