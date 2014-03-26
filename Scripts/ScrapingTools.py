#---------------------------------
# Scraping Functions for grabbing 
# draft data. 

import urllib, csv
from bs4 import BeautifulSoup


def draftScrape(webpage,outfile):
	# Function to download the source HTML of a web-page
	def download(webpage):
		page = urllib.urlopen(webpage)
		page = page.read()
		x = []
		for line in page:
			x.append(line)
		return x

	# function to output the downloaded file
	def outputPage(pageList,outfile):
		with open(outfile,'w') as out:
			for line in pageList:
				out.write(line)

	pageList = download(webpage)
	outputPage(pageList, outfile)

def parseCombineResults(infile,year):
	newStr = []
	database = []

	with open(infile,'r') as f:
		test = f.read()

	soup = BeautifulSoup(test)
	table = soup.table
	# Transform html file into a dataset...
	for td in table.find_all('td'):
		text = td.get_text()
		try:
			if(text == str(year)):
				database.append(newStr)
				newStr = [text]
			else:
				newStr.append(text)
		except Exception:
			print text
			raise "Error in parsing"
	return database

# Scrape Web Pages  - NFL combineresults .com
pageString = "http://nflcombineresults.com/nflcombinedata.php?year=2013&pos=&college="

years = xrange(1999,2015)

for i in years:
	yearStr = pageString.replace("2013", str(i))
	print yearStr
	output = '../Data/nflcombineresults.com/' + str(i) + 'draftfile.html'
	draftScrape(yearStr, output)


# From 
pageString = "http://www.cbssports.com/nfl/draft/combine/XXXX/ALL/ALL/?print_rows=9999"

years = xrange(2002,2015)

for i in years:
	yearStr = pageString.replace("XXXX", str(i))
	print yearStr
	output = '../Data/CBS Results/' + str(i) + 'draftfile.html'
	draftScrape(yearStr, output)


#-------------------------------------------
# After parsing write each years worth of 
# data to file.

csvDict = {}
years = xrange(1999,2015)

i = 1999
for i in years:
	inFile = '../data/nflcombineresults.com/' + str(i) + 'draftfile.html'	
	csvDict[i] = parseCombineResults(inFile,i)

for key in csvDict.keys():
	outName = '../Data/processedData_' + str(key) + '.csv'
	with open(outName,'wb') as outfile:
		fileWriter = csv.writer(outfile)
		for line in csvDict[key]:
			fileWriter.writerow(line)


with open(inFile) as f:
	x = f.read()

print x[0:5]
