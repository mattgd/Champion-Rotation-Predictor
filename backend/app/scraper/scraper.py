# This file scrapes the entire champion rotation history from the League of Legends wiki, and inserts it into the DB.

from datetime import date

from bs4 import BeautifulSoup
from dateutil import parser
from pygrok import Grok
import requests

from ..models.rotation import Rotation
from ..models.champion import Champion

from app import db


WIKI_URL = 'https://leagueoflegends.fandom.com'
CHAMPIONS_LIST_URL = 'http://leagueoflegends.wikia.com/wiki/List_of_champions'
CHAMPION_ROTATION_ARCHIVE_URL = 'https://leagueoflegends.fandom.com/wiki/Champion_rotation_archive'

def month_to_number(month: str):
    return {
		'January' : 1,
		'February' : 2,
		'March' : 3,
		'April' : 4,
		'May' : 5,
		'June' : 6,
		'July' : 7,
		'August' : 8,
		'September' : 9,
		'October' : 10,
		'November' : 11,
		'December' : 12
    }[month]


def to_date(dict: dict):
	"""
	Transform dictionary to Python date.
	"""
	return date(int(dict['year']), month_to_number(dict['month']), int(dict['day']))


def scrape_champions():
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')

	# Get the champion table
	trs = soup.find_all('table')[1]
	rows = trs.find_all('tr')

	# Remove table header
	rows.pop(0)

	for r in rows:
		columns = r.find_all('td')
		champion_attributes = {'name': columns[0].find('a')["title"],
							'date_released': parser.parse(columns[2].getText()),
							'subclass':columns[1].getText().strip(),
							'blue_essence':columns[4].getText(),
							'riot_points':columns[5].getText()}
		champion = Champion(**champion_attributes)
		# Add to DB session
		db.session.add(champion)

	# Save to the DB
	db.session.commit()


def scrape_rotations():
	##### Get the URL for each season's wiki page ####
	# Grab HTML
	soup = BeautifulSoup(requests.get(CHAMPION_ROTATION_ARCHIVE_URL).text, 'html.parser')

	# Access list of past champion rotations for each season
	htmlList = soup.find('div', class_='WikiaArticle').find_all('ul')[1].find_all('li')
	hrefList = []
	for l in htmlList:
		href = str(l.find('a')['href'])
		season = str(href.split('/')[-1])
		hrefList.append(WIKI_URL + href + "#" + "Pre-" + season)
		hrefList.append(WIKI_URL + href + "#" + season)

	#### Get champion and date information for each wiki ####
	week_number = 0
	date_pattern = '%{MONTHDAY:day} %{MONTH:month} %{YEAR:year}'
	grok = Grok(date_pattern)

	for url in hrefList:
		# Grab HTML
		soup = BeautifulSoup(requests.get(url).text, 'html.parser')
		# Get the table for each week of the pre-season/season
		tables = soup.find_all('table', class_='wikitable')

		# Go through each week for the pre-season/season
		for table in tables:
			# Increment the week number
			week_number += 1

			# Get the dates for that week
			dates = table.find('p').getText().replace(u'\xa0', ' ').replace(u'\n', ' ').split(" - ")
			start_date = toDate(grok.match(dates[0]))
			end_date = toDate(grok.match(dates[1]))

			# Rotation attributes dictionary
			rotation_attributes = {
				"week_number": week_number,
				"start_date": start_date,
				"end_date": end_date
			}
			rotation = Rotation(**rotation_attributes)

			# Get the list of champions for that week
			for champ in table.find_all("div", {"data-game": "lol"}):
				champion = Champion.query.filter(Champion.name == champ.find('a')['title']).first()
				if champion:
					rotation.champions.append(champion)
			
			# Add to DB session
			db.session.add(rotation)

	# Save to the DB
	db.session.commit()
