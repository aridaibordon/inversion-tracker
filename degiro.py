import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from env.config import USERNAME, PASSWORD

options             = Options()
options.headless    = True

def text_to_float(text) -> float:
    return float(text.replace(".", "").replace(",", "."))

def get_degiro_balance() -> float:
    # Returns balance of DEGIRO account
    service = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=service, options=options)

    browser.get("https://www.degiro.es/login/")

    search_username = browser.find_element(By.NAME, "username")
    search_password = browser.find_element(By.NAME, "password")
    search_enter    = browser.find_element(By.NAME, "loginButtonUniversal")

    search_username.send_keys(USERNAME)
    search_password.send_keys(PASSWORD)
    search_enter.send_keys(Keys.RETURN)

    time.sleep(10)

    search_total    = browser.find_element(By.CLASS_NAME, "uJDZaBS4")
    balance         = text_to_float(search_total.get_attribute("title"))

    return balance