from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# this will give you access to the enter key, escape key so 
# we can type something in a search bar and press enter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def launch_browser():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    # This stops from Chrome terminating automatically
    chrome_options.add_experimental_option("detach", True)
    PATH = r'/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)    
    driver.get("https://www.walmart.com")
    return driver

def search_for_product(driver, product_name):
    search_results = driver.find_element_by_id("global-search-input")
    # search for the product using the name
    search_results.send_keys(product_name)
    search_results.send_keys(Keys.RETURN)    


def select_store(driver):
    check_walmart = driver.find_element_by_id("Walmart.com-0-retailer")
    check_walmart.click()

driver = launch_browser()
search_for_product(driver, r'2020 select football cards')
select_store(driver)
