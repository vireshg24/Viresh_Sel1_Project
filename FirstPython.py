
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_and_scrape():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    username = "student"
    password = "Password123"
    button_selector = "your_button_selector"
    driver.get('https://practicetestautomation.com/practice-test-login/')
    time.sleep(2)
    # Perform login
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()

    # Wait for the page to load

    time.sleep(2)
    driver.close()
    driver.quit()
