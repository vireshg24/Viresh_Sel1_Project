import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def login_and_scrape():
    username="student"
    passwrod="Password123"
    url="https://practicetestautomation.com/practice-test-login/"
    chrome_path="E:\softwares\selenium\chromedriver-win64\chromedriver.exe"
    button_selector = "2431"

    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    # Wait for the page to load
    time.sleep(2)

    # Perform login
    driver.find_element("username").send_keys(username)
    driver.find_element("password").send_keys(passwrod)
    driver.find_element_by_name("submit").click()

    # Scraping logic
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Replace 'your_number_element_selector' with the actual selector for the element containing the number
    number = int(soup.select_one('your_number_element_selector').text)

    # Check if the number is greater than 0
    if number == 0:
        # Click on the button
        driver.find_element_by_css_selector(button_selector).click()
        print("Button clicked!")

    # Close the browser window
    driver.quit()

# Run the script every 10 minutes
while True:
    login_and_scrape()
    time.sleep(600)  # Sleep for 10 minutes (600 seconds)