from bs4 import BeautifulSoup
from smtplib import SMTP
import requests
import re
import sqlite3

def scrape(search_term, distance):
	results = []
	URL = """http://www.gumtree.com/search?q=%s&category=freebies&
	search_location=Walthamstow%%2C+London&distance=%s&
	current_distance=&min_price=&max_price=""" % (search_term, distance)


	r = requests.get(URL)
	data = r.text

	soup = BeautifulSoup(data)
	regex = re.compile('/for-sale/')

	for link in soup.find_all('a'):
		
		anchor = link.get('href')

		if regex.search(str(anchor)) != None:
			results.append(str(anchor))

	return results


def store_results(results):
	conn = sqlite3.connect('scrapey.db')



	for i in results:
		query = "SELECT link FROM ADS WHERE link = '" + i + "'"
		insert = "INSERT INTO ADS (link, description, posted) VALUES ('" + i + "', null, null)"
		print query
		print insert
		cursor = conn.execute(query)

		if cursor.fetchone() is None:
			conn.execute(insert)
			conn.commit()

def send_email(email, message):
	fromaddr = "Scrapey"
	msg = ("From: {0}\n\nTo:{1}\n\n\n\n\nCheck these:\n\n{2}").format(fromaddr,email,message)

	
res = scrape("desk", "1.0")
store_results(res)
