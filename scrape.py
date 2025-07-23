import selenium.webdriver as webdriver

from selenium.webdriver.firefox.service import Service     #Remove Comment If Using Firefox 
# from selenium.webdriver.chrome.service import Service      #Remove Comment If Using Chrome 

import time


def scrape_website(website):
    print("Launching Browser ....")

    driver_path = "./geckodriver"
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=Service(driver_path),options=options)

    # driver_path = "./chromedriver"  # Remove Comment If Using Chrome 
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=Service(driver_path),options=options)  

    try:
        driver.get(website)
        print("Loading Site")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()