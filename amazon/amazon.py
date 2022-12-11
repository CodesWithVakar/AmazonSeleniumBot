
import os
import amazon.constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from amazon.customdriver import CustomDriver
import csv
import pandas as pd
import numpy as np
import xlsxwriter
from xlsxwriter.workbook import Workbook
import numpy as np
import openpyxl
from pathlib import Path



class Amazon(WebDriver):
    def __init__(self, driver):
        self.driver = driver
        
    def first_page(self):
        self.driver.get(const.BASE_URL)

    def item_search(self,search):
        search_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.nav-search-field>input")))
        search_field.send_keys(search)
    
    def take(self):
        first_result = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.autocomplete-results-container>div>.s-suggestion-container")))
        first_result.click()

    def maxPrice(self,max_price):
        item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#high-price")))
        item.send_keys(max_price)

        item_filter = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.a-button-input")))
        item_filter.click()

    def minPrice(self,min_price):
        item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#low-price")))
        item.send_keys(min_price)

        item_filter = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.a-button-input")))
        item_filter.click()

    def sort_by_low(self):
        sort_by_low = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-button-text.a-declarative")))
        sort_by_low.click()
        time.sleep(0.7)
        low = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li>#s-result-sort-select_1")))
        low.click()
  
    def sort_by_high(self):
        sort_by_high = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-button-text.a-declarative")))
        sort_by_high.click()
        time.sleep(0.7)
        high = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li>#s-result-sort-select_2")))
        high.click()

    def shoeSize(self,value):
        shoesize = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//button[@value={value}]")))
        shoesize.click()

    def size(self,xsize):
        size = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//button[@value={xsize}]")))
        size.click()

    def review(self,star):
        review = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"i.a-star-medium-{star}")))
        review.click()

    def report(self):
        items = self.driver.find_elements(By.XPATH, "//*[contains(@cel_widget_id,'MAIN-SEARCH')]")
        
        item_list= []
        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal').text
                price = item.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                item_list.append([title, "$"+ price])
            except:
                continue
        
       
        absolute_path = os.path.abspath(__file__ + "/../../")
        csv_file_name = "list_item.csv"
        excel_file_name = "list_item.xlsx"

        csv_full_path = os.path.join(absolute_path, "output", csv_file_name)
        excel_full_path = os.path.join(absolute_path, "output", excel_file_name)

        np.savetxt(csv_full_path, item_list, delimiter=", ", header='Product Name, Price', fmt='% s')
        df = pd.DataFrame(item_list, columns=["Product Name", "Price"])
        
        with pd.ExcelWriter(excel_full_path) as writer:
            df.to_excel(writer, sheet_name="ItemList")  

        
        