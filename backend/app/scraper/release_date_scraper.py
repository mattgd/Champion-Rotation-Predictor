import requests
from bs4 import BeautifulSoup
from dateutil import parser

from app import db
from ..models.champion import Champion

url = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'

def scape():
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')

	#Get the champion table
	trs = soup.find_all('table')[1]
	rows = trs.find_all('tr')
	#Remove table header
	rows.pop(0)
	for r in rows:
		columns = r.find_all('td')
		champion_attributes = {'name': columns[0].find('a')["title"],
							'date_released': parser.parse(columns[2].getText()),
							'subclass':columns[1].getText().strip(),
							'blue_essence':columns[4].getText(),
							'riot_points':columns[5].getText()}
		champion = Champion(**champion_attributes)
		db.session.add(champion)

	db.session.commit()
