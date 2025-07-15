from bs4 import BeautifulSoup
import requests
def get_rateCurrency(in_currency, out_currency, amount):
    URL =f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content= requests.get(URL).text
    soup=BeautifulSoup(content, 'html.parser')
    rate=soup.find("span", class_="ccOutputRslt").get_text()
    return float(rate[:-4])

in_currency = input("enter the currency: ")
out_currency = input("enter the currency: ")
amount = input("enter the amount of currency: ")

rate = get_rateCurrency(in_currency, out_currency, amount)
print(rate)