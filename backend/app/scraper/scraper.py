# This file scrapes the entire champion rotation history from the League of Legends wiki,
# and sends the data in a POST request to a PHP script to handle the data.

import json
import requests
from bs4 import BeautifulSoup
from pygrok import Grok
from datetime import date

from ..models.rotation import Rotation
from app import db

def monthToNum(mon):
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
    }[mon]

#Function to transform dictionary to python date
def toDate(dic):
	return date(int(dic['year']),monthToNum(dic['month']),int(dic['day']))


#Wiki
wiki='https://leagueoflegends.fandom.com'
#Champion rotation archive link
url = 'https://leagueoflegends.fandom.com/wiki/Champion_rotation_archive'

#### Get the URL for each season's wiki page ####
# Grab HTML
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# Access list of past champion rotations for each season
htmlList = soup.find('div',class_='WikiaArticle').find_all('ul')[1].find_all('li')
hrefList = []
for l in htmlList:
	href=str(l.find('a')['href'])
	season=str(href.split('/')[-1])
	hrefList.append(wiki + href+"#"+"Pre-"+season)
	hrefList.append(wiki + href+"#"+season)



#### Get champion and date information for each wiki ####
weekNum = 0
date_pattern = '%{MONTHDAY:day} %{MONTH:month} %{YEAR:year}'
grok = Grok(date_pattern)


for url in hrefList:
	#Grab HTML
	soup = BeautifulSoup(requests.get(url).text, 'html.parser')
	#Get the table for each week of the pre-season/season
	tables = soup.find_all('table',class_='wikitable')
	#Go through each week for the pre-season/season
	for table in tables:
		# Increment the week number
		weekNum += 1
		#Get the dates for that week
		dates = table.find('p').getText().replace(u'\xa0', ' ').replace(u'\n', ' ').split(" - ")
		start_date = toDate(grok.match(dates[0]))
		end_date = toDate(grok.match(dates[1]))
		#get the list of champions for that week
		champions = []
		for champ in table.find_all("div", {"data-game": "lol"}):
			champions.append(champ.find('a')['title'])
		#Insert into DB

        champion = Champion()
		print(weekNum, end="  ")
		print(start_date, end="  ")
		print(end_date, end="  ")
		print(champions)
