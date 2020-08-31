import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

#structure = {'name' : [], 'hp' : [], 'str' : [], 'mag' : [], 'dex' : [], 'spd' : [], 'lck' : [], 'def' : [], 'res' : [], 'cha' : []}
#df = pd.DataFrame(data = structure)
#
#print(df)
#print('\n'*3)
#
#URL = 'https://serenesforest.net/three-houses/classes/growth-rates/'
#page = requests.get(URL)
#
#soup = BeautifulSoup(page.content, 'html.parser')
#
#broth = soup.find(class_="entry")
#results = soup.find_all('table')
#
#for index, result in enumerate(results):
#	x = result.find_all('td')
#	l = list()
#	for i , y in enumerate(x):
#		z = y.text
#		if y.text.endswith('\n'):
#			z = y.text[:-1]
#		if i%10 != 9:
#			if z == '\xa0':
#				l.append('0')
#			elif z != '\xa0':
#				l.append(z)
#		elif i%10 == 9:
#			if z == '\xa0':
#				l.append('0')
#			elif z != '\xa0':
#				l.append(z)
#				insert = pd.Series(data = l, index = df.columns, name = len(df) + 1)
#				df = df.append(insert)
#			print(l)
#			del(l[:])
#
#print(df)
#
#df.to_csv('ClassGrowths.csv')





