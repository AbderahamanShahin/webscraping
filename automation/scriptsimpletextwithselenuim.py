from selenium import webdriver
import time
URL = input("enter the url of website you want to scrip from it: ")
def clean_text(text):
    output = float(text.split(":")[2])
    return output
# this lines used to make scrip easier
def get_driver(URL):
    options = webdriver.ChromeOptions()
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
    element = driver.find_element(by="xpath", value="/html/body/div[6]/div[2]/div/div[1]/div[2]")
    return clean_text(element.text)

print(main())
