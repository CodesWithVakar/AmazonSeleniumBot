from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from amazon.customdriver import CustomDriver


class Filters(WebDriver):
    def __init__(self, driver):
        self.driver = driver
    
    def Price(self,max_price):
        item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#high-price")))
        item.send_keys(max_price)

        item_filter = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.a-button-input")))
        item_filter.click()
