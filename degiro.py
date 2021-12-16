import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

USERNAME, PASSWORD = os.environ["USERNAME"], os.environ["PASSWORD"]

def text_to_float(text) -> float:
    return float(text.replace(".", "").replace(",", "."))

def get_degiro_balance() -> float:
    # Returns balance of DEGIRO account
    browser = webdriver.Chrome(ChromeDriverManager().install())

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