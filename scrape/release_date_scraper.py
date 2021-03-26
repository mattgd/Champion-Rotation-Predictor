import os
import json
import requests
from bs4 import BeautifulSoup


url = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

#Get the champion table
trs = soup.find_all('table')[1]
rows = trs.find_all('tr')
#Remove table header
rows.pop(0)
for r in rows:
	columns = r.find_all('td')
	#Get name
	print(columns[0].find('a')["title"])
	#Get release date
	print(columns[2].getText())
	#Get BE cost
	print(columns[4].getText())
	#Get RP cost
	print(columns[5].getText())
