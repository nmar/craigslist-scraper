from bs4 import BeautifulSoup
import urllib2
import re
import os

page = urllib2.urlopen('http://www.craigslist.org/about/sites')
soup = BeautifulSoup(page)

# change working directory to out/ so we don't mix code and results
os.chdir("out/")

# go through the soup, look for a state_delimiter stop at each one, find the ul and list the a tags in there

# lets look at the first continent USA
usa = soup.find("div", attrs={'class':'colmask'})

# this cycles 50 times looking for the class called state_delimiter
# once that is found, it looks for the ul following it and inside that looks for the href
for i in range(0,51):
	statespace = usa.find_all("div", attrs={'class':'state_delimiter'})[i].string
	# remove space from state names
	state = re.sub(r'\s', '', statespace)
	statename = open(state+".txt", "w")
	url = usa.find_all("div", attrs={'class':'state_delimiter'})[i].find_next("ul").find_all("a",href=re.compile("^http."))
	# for each href found add it to the state.txt file
	for link in url:
		statename.write(link.get('href'))
		statename.write("\n")
	statename.close()

