#---------------------------------
# Scraping Functions for grabbing 
# draft data. 

import urllib

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

# Scrape Web Pages
pageString = "http://nflcombineresults.com/nflcombinedata.php?year=2013&pos=&college="

years = xrange(1999,2014)

for i in years:
	yearStr = pageString.replace("2013", str(i))
	print yearStr
	output = str(i) + '..\Data\draftfile.html'
	draftScrape(yearStr, output)

