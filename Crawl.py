import urllib2
import urllib 
from urllib2 import HTTPError, URLError
from bs4 import BeautifulSoup

def Crawler(url):
	#urllib helps to automatically detect the type of URL and fetch it accordingly.
	#Fake user agent to be a Mozilla Browser to be consistent since some websites may dislike the user agent being a program!
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	#We are assuming that encoding is not required but can easily specify it if required. 
		
	opener = urllib2.build_opener()
	opener.addheaders = [('User-Agent', user_agent)]

	try:
		response = opener.open(url) #Is the URL accessible?
	except HTTPError as e:
		print 'The server could not fulfill the request'
	except URLError as e:
		print 'We failed to reach the server.'
		print "reason:". e.reason #contains all the HTTP errors. 
	the_page = response.read() #Store the page
	soup = BeautifulSoup(the_page, 'html.parser') #Create a soup object 
	return soup #And, return it!
