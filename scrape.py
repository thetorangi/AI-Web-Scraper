import selenium.webdriver as webdriver

# from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.service import Service 
import time


def scrape_website(website):
    print("Launching Browser ....")

    driver_path = "./geckodriver"
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=Service(driver_path),options=options)

    try:
        driver.get(website)
        print("Loading Site")
        html = driver.page_source
        time.sleep(10)

    finally:
        driver.quit()

print("Test")