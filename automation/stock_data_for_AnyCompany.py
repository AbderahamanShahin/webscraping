import time
import requests
from datetime import datetime
ticker = input("Enter ticker you want: ")
from_date= datetime.strptime(input("Enter the date yoa want start in format YYYY/MM/DD: " ), '%Y/%m/%d')
to_date= datetime.strptime(input("Enter the date yoa want end in format YYYY/MM/DD: " ), '%Y/%m/%d')

URL = f"https://finance.yahoo.com/quote/{ticker}/history/?period1={int(time.mktime(from_date.timetuple()))}&period2={int(time.mktime(to_date.timetuple()))}"
header = {"User-Agent": "Mozilla/5.0 (X11; Linux X86_64) AppleWebkit/537.36 (KHTML, like Gecko) Chorme/88.04324.96 Safari/537.36"}
content = requests.get(URL, headers=header).content
print(content)
with open("stockdata.csv", 'wb') as file:
    file.write(content)