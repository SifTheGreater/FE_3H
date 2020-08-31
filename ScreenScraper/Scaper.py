
import requests
from bs4 import BeautifulSoup
import sqlite3


def sqlite_table_schema(conn, name):
	cur = conn.execute("SELECT sql FROM sqlite_master WHERE name=?;", [name])
	sql = cur.fetchone()[0]
	cur.close()
	print(sql)


conn = sqlite3.connect("tea.db")
c = conn.cursor()

#sqlite_table_schema(conn, 'Teas')



#the below code scans the serene forest page for the tea data and ill use it to fill out tables

URL = 'https://serenesforest.net/three-houses/monastery/tea-party/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup, file = open('htmlData.txt', 'a'))

results = soup.find(class_="entry")
#print(results.prettify())

Names = results.find_all('a')

name = list()
for x in Names:
	y = x.text
	#print(x.text)
	if y.endswith('\n'):
		y = x.text[:-1]
	name.append(y)

here = list()
here.append(name[0])

for name in name:
	url = URL + name
	#print(url)
	tea_choices = list()


	page2 = requests.get(url)

	soup2 = BeautifulSoup(page2.content, 'html.parser')

	results2 = soup2.find(class_="entry")

	Teas = results2.find_all("table")

	#print(len(Teas))
	
	tea = Teas[0]
	questions = Teas[2]

	for index, single in enumerate(Teas):
		if index == 0:
			t = single.find_all('td')
			
			for index1, x in enumerate(t):
				if index1%3 == 0:
					a = x.text
				elif index1%3 == 1:
					b = x.text
				elif index1%3 == 2:
					sqlite_insert_with_param = "INSERT INTO Teas(Name, Tea1, Tea2, Tea3)VALUES (?, ?, ?, ?);"
					data_tuple = (name, a, b, x.text)
					c.execute(sqlite_insert_with_param, data_tuple)

		if index == 2:

			t = single.find_all('td')
			
			y = 0
			for index3, x in enumerate(t):
				if index3%4 == 0:
					q = x.text
				elif index3%4 == 1:
					a = x.text
				elif index3%4 == 2:
					b = x.text
				elif index3%4 == 3:
					sqlite_insert_with_param = "INSERT INTO Questions(Name, Question, Ans1, Ans2, Ans3) VALUES (?, ?, ?, ?, ?);"
					data_tuple = (name, q, a, b, x.text)
					c.execute(sqlite_insert_with_param, data_tuple)



conn.commit()
conn.close()
