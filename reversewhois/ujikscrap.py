from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs4


site = input("Enter Domain Name : ")
url = ('https://viewdns.info/reversewhois/?q=' + site)
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
webpage = html.decode('utf-8')
soup = bs4(webpage, "html.parser")


result = soup.find_all("table", attrs={"border" : "1"})

for i in result:
	row = ''
	rows = i.findAll('tr')
	for row in rows:
		print(row.getText(' '))

