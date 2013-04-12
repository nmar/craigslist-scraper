craigslist-scraper 
==================

A Python scraper for Craigslist lost and found ads in all U.S. states,
using BeautifulSoup.

I used this very basic little script to comb Craigslist ads for lost
iPhones.

It's made of two Python scripts:

* clstates.py opens the URL ('http://www.craigslist.org/about/sites')
and extracts from it the Craigslist sites for each U.S. state, putting
the site URL name into a .txt file. These .txt files go into a working
directory called "out/"

* clads.py looks inside "out/" directory, for each CL site builds the
lost and found search URL and attaches the search key "iphone"; it
iterates through the search results to extract the ad content and
drops it into a file called out-STATENAME.txt

The code tries to play nice with the CL server, taking plenty of breaks. 

Known issues
=================

The script needs to be executed in one go, it doesn't deal well with
network interruptions since it does not keep track of what has already
been done. 