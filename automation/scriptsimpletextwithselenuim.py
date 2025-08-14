from selenium import webdriver
import time
URL = input("enter the url of website you want to scrip from it: ")
def clean_text(text):
    output = float(text.split(":")[2])
    return output
# this lines used to make scrip easier
def get_driver(URL):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")           # Run in headless mode (no UI)
    options.add_argument("--disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver =webdriver.Chrome(options=options)
    driver.get(URL)
    return driver

def main():
    driver = get_driver(URL)
    time.sleep(10)
    element = driver.find_element(by="xpath", value="/html/body/main/div[3]/div/div[3]/div/div/div[16]/div[3]/h3/a")
    return element.text

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(main())