# install selenium
# install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://app.everrise.com/everown/list")

def findCustomersEverOwn():
    data = WebDriverWait(browser, 10).until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME,
             "css-gz2zj8")))
    return len(data)

print(findCustomersEverOwn())

