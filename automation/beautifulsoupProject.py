import csv
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
wazefa = input("Enter the job you are searching on it: ").strip()
URL = requests.get(f"https://wuzzuf.net/search/jobs/?q={wazefa}&a=navbl")
src = URL.content
soup = BeautifulSoup(src, 'html.parser')

job_test= soup.find_all("h2", class_="css-m604qf")
location_test = soup.find_all("span", class_="css-5wys0k")
company_test= soup.find_all("a", class_="css-17s97q8")
skill_test = soup.find_all("div", class_="css-y4udm8")

job=[]
location=[]
company=[]
skills=[]
links=[]
salary = []
for i in range(len(job_test)):
    job.append(job_test[i].get_text())
    links.append(job_test[i].find("a").attrs['href'])
    location.append(location_test[i].get_text())
    company.append(company_test[i].get_text().replace("-", ""))
    skill=skill_test[i].get_text()[15:]
    if skill.startswith("e"):
        skill = skill[1:]
        skills.append(skill)
    else:
        skills.append(skill)

content =zip_longest(job, location, company, skills, links, salary)
with open("wazefa.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title", "Location", "Company", "Skills", "Links", "Salary"])
    writer.writerows(content)