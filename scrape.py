from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

''' The Below Block is for Testing Purpose

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

'''

def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html


