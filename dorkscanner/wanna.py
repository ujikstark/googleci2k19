## Created By Ujikstark

#!/usr/bin/env python3
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs4
from fake_useragent import UserAgent

fake = UserAgent().random

def in_google():
	url = ('https://www.google.com/search?q='+ dork + '&num=100&hl=en&start=0')
	req = Request(url, headers={'User-Agent': fake})
	html = urlopen(req).read()
	webpage = html.decode('utf-8')
	soup = bs4(webpage, "html.parser")

	result = soup.findAll('cite', attrs={'class':'iUh30'})
	url_result = []

	for i in result:
		try:
			url_result.append(i.text)
		except:
			pass
	for x in url_result:
		print(x)
		
def in_bing():
	url = ('https://www.bing.com/search?q=' + dork + '&count=100')
	req = Request(url, headers={'User-Agent': fake})
	html = urlopen(req).read()
	webpage = html.decode('utf-8')
	soup = bs4(webpage, "html.parser")
	
	result = soup.findAll('li', class_='b_algo')
	url_result = []
	
	for i in result:
		try:
			url_result.append(i.find('a').attrs['href'])
		except:
			pass		
	for x in url_result:
		print(x)

dork = input("Your Dork $ ")

print("1 = Google\n2 = Bing\nYou can type 1 or 2")
searching = input("Searching : ")
			
if searching is '1':
	in_google()
elif searching is '2':
	in_bing()
else:
	print("ERROR!!")
	
