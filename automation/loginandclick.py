from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
URL = input("enter the url of website you want to scrip from it: ")
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
    driver.find_element(by="xpath", value="/html/body/div/div[3]/div/div[1]/div[1]/div/div/header/div/div/div[4]/div/nav/ul/li[3]/a").click()
    time.sleep(4)
    driver.find_element(by="xpath", value="/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("headline57@outlook.com" + Keys.RETURN)
    time.sleep(4)
    driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/form/div[2]/div/div[4]/div[1]/div/span/input").send_keys("305052AS" + Keys.RETURN)
    time.sleep(4)
    driver.find_element(by="xpath", value="/html/body/div/div/div/div/div/div[1]/div/div/div/div/form/div[2]/div/div[5]/button[2]").click()
    time.sleep(4)

main()
