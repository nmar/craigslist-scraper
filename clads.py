import urllib2
from bs4 import BeautifulSoup
import re
import time
import os
from os import listdir
from os.path import isfile, join

# set the working directory
wd = "out/"
# set the search keyword
key = "iphone"
onlyfiles = [f for f in listdir(wd) if isfile(join(wd,f))]

# read the states.txt files from the working directory
# for each file in the working directory
for myfile in onlyfiles:
	workingfile = open(wd+myfile, "r")
	print "myfile is: " + myfile

	# for each line in the file
	# go to the results page and identify the URLs of the ad

	for line in iter(workingfile):
		requesturl = line.rstrip("\n") + "/search/laf?zoomToPosting=&query=" + key + "&srchType=A"
		print "The result url is: " + requesturl
		request = urllib2.Request(requesturl)
		request.add_header('User-agent', 'Mozilla 5.10')
		resultpage = urllib2.urlopen(request)
		results = BeautifulSoup(resultpage)
		listURL = results.findAll('a', href=re.compile("^http.*\/laf\/"))
		# for each URL go ge the ad content
		for ad in listURL:
		 	adurl = ad.get('href')
			reqadpage = urllib2.Request(adurl)
			reqadpage.add_header('User-agent', 'Mozilla 5.10')
			adpage = urllib2.urlopen(reqadpage)
			print "Now go to get them: " + adurl
			bspage = BeautifulSoup(adpage)
			adcontent = bspage.find("section", id="postingbody").stripped_strings
			for cleancontent in adcontent:
				content = repr(cleancontent)
				print "The content cleaned up is: " + content
				outfile = open(wd+"out-" + myfile, "a")
				print "Dropping content into: " + outfile.name
				outfile.write(content)
			outfile.close()
			# cycle through the adurl and go get the content

			time.sleep(10)
	workingfile.close()
	time.sleep(60)
