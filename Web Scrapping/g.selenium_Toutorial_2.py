# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec


# chrome_driver_path = "/home/silk2023/Downloads/akshay/cdriver/chromedriver-linux64/chromedriver"
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)
# https://quotes.toscrape.com/js/

# wait = WebDriverWait(driver,10)
# quote_element = wait.until(ec.presence_of_element_located((By.CLASS_NAME,"quote")))

# quote = quote_element.find_element(By.CLASS_NAME,"text").text
# author = quote_element.find_element(By.CLASS_NAME,"author").text

# print(quote," - ", author)

# driver.quit()



#------------------------------  For Multiple quotes ------------------------------#


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By


# chrome_driver_path = "/home/silk2023/Downloads/akshay/cdriver/chromedriver-linux64/chromedriver" 
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# url = "https://quotes.toscrape.com/js/"
# driver.get(url)

# wait = WebDriverWait(driver,10)
# quote_elements = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME,"quote")))


# for quote_element in quote_elements:
#     quote = quote_element.find_element(By.CLASS_NAME,"text").text
#     author = quote_element.find_element(By.CLASS_NAME,"author").text

#     print(f"{quote} -- {author}")


# driver.quit()


#-------------------------------- Scrapping across all pages --------------------------------#


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException


# chrome_driver_path = ""
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service = service)

# driver.get("https://quotes.toscrape.com/js/")
# wait = WebDriverWait(driver,10)

# while True:
#     quote_elements = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME,"quote")))
#     for quote_element in quote_elements:
#         quote = quote_element.find_element(By.CLASS_NAME,"text").text
#         author = quote_element.find_element(By.CLASS_NAME,"author").text

#         print(f"{quote}----{author}")

#     try:
#         next_button = driver.find_element(By.CLASS_NAME,"next")
#         next_link = next_button.find_element(By.TAG_NAME,"a")
#         next_link.click()

#     except NoSuchElementException as e:
#         print("All Pages Scrapped successfully..")
#         break


# driver.quit()


#----------------- Writing data into csv file ----------------#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import csv

chrome_driver_path = "/home/silk2023/Downloads/akshay/cdriver/chromedriver-linux64/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com/js/")

wait = WebDriverWait(driver,10)

with open("quotes.csv",mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quotes","Author"])

    while True:
        quote_elements = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME,"quote")))

        for qe in quote_elements:
            quote = qe.find_element(By.CLASS_NAME,"text").text
            author = qe.find_element(By.CLASS_NAME,"author").text

            print(f"{quote} --- {author}")

            writer.writerow([quote,author])
        try:
            next_button = driver.find_element(By.CLASS_NAME,"next")
            next_link = next_button.find_element(By.TAG_NAME,"a")
            next_link.click()
        except NoSuchElementException:
            print("All pages Scrapped successfully")
            break

driver.quit()





#-------------------  Practice ----------------------#

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException


# chrome_driver_path = "/home/silk2023/Downloads/akshay/cdriver/chromedriver-linux64/chromedriver"
# service = Service(executable_path=chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# driver.get("https://quotes.toscrape.com/js/")

# wait = WebDriverWait(driver,10)

# while True:
#     quote_elements = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME,"quote")))

#     for quote_element in quote_elements:
#         quote = quote_element.find_element(By.CLASS_NAME,"text").text
#         author = quote_element.find_element(By.CLASS_NAME,"author").text

#         print(f"{quote}----{author}")

#     try:
#         next_button = driver.find_element(By.CLASS_NAME,"next")
#         next_link = next_button.find_element(By.TAG_NAME,"a")
#         next_link.click()

#     except NoSuchElementException:
#         print("All Pages Scrapped successfully..")
#         break

# driver.quit()


