from bs4 import BeautifulSoup
import requests

URL = requests.get("https://khamsat.com/programming").text
soup = BeautifulSoup(URL, "html.parser")
categories = soup.find_all("h3", class_="mb-3 grid-items--title")
category = []
for categ in categories:
    category.append(categ.get_text())

print(category)