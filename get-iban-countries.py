import requests
from bs4 import BeautifulSoup

f = open('iban-data.txt', 'w')

URL = "https://www.iban.com/structure"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

data = []
table = soup.find('table', attrs={'class':'table'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

indices = 2, 4
for i in range(len(data)):
    list1 = data[i]
    list1 = [i for j, i in enumerate(list1) if j not in indices]
    f.write("%s\n" % ",".join(list1))

f.close()
