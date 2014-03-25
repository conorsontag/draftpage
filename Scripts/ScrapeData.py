#-------------------------------------------------------
# Script for grabbing out data of interest from 
# combine result web pages. 

import os
from bs4 import BeautifulSoup

with open("../Data/nflcombineresults.com/2013draftfile.html") as file:
	test = file.read()

# Create a beautiful soup object.
soup = BeautifulSoup(test)

table = soup.table

iter = 0
for td in table.find_all('td'):
	if(iter > 40):
		break
	else:
		print td.get_text()
		iter += 1