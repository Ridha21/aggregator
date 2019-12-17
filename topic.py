import urllib.request
from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.dailymail.co.uk/home/latest/index.html","lxml")
soup = BeautifulSoup(page.content)

gData = soup.find_all("a",{"class": "title"})
for item in gData:
	print (item.text)
