import time
from selenium import webdriver
from datetime import datetime as dt
from selenium.webdriver.common.keys import Keys

URL = input("enter the url of website you want to scrip from it: ")
def clean_text(text1):
    output = float(text1.split(":")[2])
    return output
def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, "w") as file:
        file.write(text)
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
    while True:
        time.sleep(5)
        element = driver.find_element(by="xpath", value="/html/body/div[6]/div[2]/div/div[1]/div[2]")
        output = clean_text(element.text)
        write_file(str(output))


main()
