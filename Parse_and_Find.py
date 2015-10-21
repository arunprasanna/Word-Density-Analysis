import Crawl
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
from nltk.stem import WordNetLemmatizer
import collections
import itertools

lmtzr = WordNetLemmatizer()
dict_of_words = collections.OrderedDict()

#Comment out the following line if you have installed the packages and the window is irritating you!
#nltk.download()

#stop now contains all the stop words in english. We Don't include these words in our analysis. 
stop =  stopwords.words("english")

#Prompt for the url to crawl and store it in url. 
url = raw_input('Enter the url to be crawled: ')

number_of_results = int(raw_input('Enter the number of keywords you need: '))



#parsed now contains the soup object that has been created.
#please check the other file Crawl.py for details on how the crawler works. 
parsed = Crawl.Crawler(url)

#Add or remove html tags you may not be interested in. 
#The below list is only a sample and yes, I know that including some these
#may result in better results. 

uninterested = ["script", "div", "option", "input", "span", "li", "img", "style"]
#uninterested=[]

#Create a dictionary of weigths containing how important,
#the occurence of the word is. Example: URL weight more important than title which is much 
#more important than normal ocurrences. 
#we can extend this dictionary as required. Easily scalable. 

"""These weights are extremely crucial and I've achieved good results by playing with them for different pages. 
	Need to test more to find a consistent set of weights that work well universally. 
"""
weights ={"url" : 44, "title": 64, "header" : 10, "normal":0.01}

#We can have as many distinctions as we need to store different strings in
#different lines. We can directly use just the dict and save memory but I have gone 
#with this implementation to help debug and show the scalability of the code. 
header_lines = []
normal_lines = []

"""The following function removes all stop words.
	ascii error handled. 
	Returns a list of words without the stop words. 
"""
def remove_stop_words(string):
	try:
		string_list = string.split()
		final_list = []
		for word in string_list:
			if word not in stop:
				final_list.append(word)
	except UnicodeEncodeError:
		return False
	return final_list

"""The following function lemmatizes a list of strings. 
	The function call has been commented out in the implementation.
	Need to test more to see if it is required for our sample space of words.
"""
def lemmatize(string_list):
	final_list = []
	for word in string_list:
		final_list= lmtzr.lemmatize(word)
	return final_list

"""Function to add a key,value pair to the dictionary. 
	The type determines the weight it gets and thus
	the value to be added to the key.
"""
def add_to_dict(string_list, type):
	for word in string_list:
		#Make sure to convert to lower case before creating the entry in dict. 
		word = word.lower()
		if word in dict_of_words:
			if "none" not in word and len(word)>4:
				existing_weight = dict_of_words[word]
				dict_of_words[word] = existing_weight+ weights[type]
		else:
			if "None" not in word:
				dict_of_words[word] = weights[type]

"""Prints the dictionary. 
	Assumes a sorted OrderedDict. 
"""
def print_dictionary(value):
	x =  itertools.islice(sorted_by_value.items(),7 ,value+7)
	for key,value in x:
		print key,
		print "\t:\t",
		print value,
		print "\n"

"""A two level html parse-tree search.
	Classifies strings as header and normal strings. 
	Some error handling done. 
	Can also further classify into different headers, 
	different tags etc. For example give a separate weights for ocurrences 
	in the image caption. Just shown a sample here. 
"""
def read_body_and_update():
	for level1_tags in parsed.find_all(True):
		if level1_tags.name not in uninterested:
			if level1_tags.name and level1_tags.name:
				if "h" in level1_tags.name:
					header_lines.append(level1_tags.string)
					try:
						split_string = remove_stop_words(str(level1_tags.string))
					except UnicodeEncodeError:
						pass
					if split_string:
						add_to_dict(split_string,'header')
				else:
					normal_lines.append(level1_tags.string)
					try:
						split_string = remove_stop_words(str(level1_tags.string))
					except UnicodeEncodeError:
						pass
					if split_string:
						add_to_dict(split_string,'normal')
					normal_lines.append(level1_tags.string)
					for level2_tags in parsed.find_all(level1_tags.name):
						if level2_tags.name and level2_tags.string:
							if "h" in level2_tags.name:
								header_lines.append(level2_tags.string)
								try:
									split_string = remove_stop_words(str(level2_tags.string))
							 	except UnicodeEncodeError:
							 		pass
							 	if split_string:
									add_to_dict(split_string,'header')
							else:
								normal_lines.append(level2_tags.string)
								try:
									split_string = remove_stop_words(str(level1_tags.string))
								except UnicodeEncodeError:
									pass
								if split_string:
									add_to_dict(split_string,'normal')


"""Function to check if the top results in the dictionary exist in the 
   title of the page. Update value in dict accordingly. 
 """
def read_title_and_update():
	title= str(parsed.title.string)
	#We are interested in updating only the top certain result's values. Say, 500. 
	x =  itertools.islice(sorted_by_value.items(),0 ,500)
	for key, value in x:
		if len(key) > 4:
			if key in str(title):
				existing_value = dict_of_words[key]
				dict_of_words[key]= existing_value+ weights['title']

"""Function to check if the top results in the dictionary exist in the 
   url of the page. Update value in dict accordingly. URL used is the url body and
   not the first part of the URL.
 """			
def read_url_and_update():
	#We are not interested in the domain name, only in the rest of the URL.
	#Not RIGOROUS. ASSUMES A .COM WEBSITE for now
	#URL_SPLIT = [".com", ".net", ".gov", ".edu"]
	#
	url_string = url.split(".com")[1]
	x =  itertools.islice(sorted_by_value.items(),0 ,500)
	for key, value in x:
		if len(key) > 4:
			if key in str(url_string):
				existing_value = dict_of_words[key]
				dict_of_words[key] = existing_value + weights['url']



read_body_and_update()
sorted_by_value = collections.OrderedDict(sorted(dict_of_words.items(), key = lambda x: x[1]), reverse=True)
read_title_and_update()
sorted_by_value = collections.OrderedDict(sorted(dict_of_words.items(), key = lambda x: x[1]), reverse=True)
read_url_and_update()
sorted_by_value = collections.OrderedDict(sorted(dict_of_words.items(), key = lambda x: x[1], reverse=True))
print_dictionary(number_of_results)

						


