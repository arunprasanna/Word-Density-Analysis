--------------README FOR WORD DENSITY ANALYZER--------------
CONTAINS: 
---------
Crawl.py -  Crawler built in Python using urllib and Beautiful Soup. Handles all HTTP errors and fakes User agent to be a Mozilla Browser. Check code for details. 
Parse_and_Find.py - Several methods(functions) have been defined. The code takes the soup object as input from the Crawler and prints out the most ocurring words. Remember that the weights assigned are not optimal. The idea has been to show the complexity of the task and think of what we can do. 

--------
USAGE:
--------
Type python Parse_and_Find.py

to run the script. It automatically builds the Crawler module. 

---------------
DEPENDENCIES:
---------------
Ensure that Crawl.py is available in the same directory as the Parse_and_Find.py scirpt. (OR Ensure it is accessible by copying it into /usr/bin/local)

Beautiful Soup and nltk modules are required to be installed. 

IN Linux(Debian) : PLease check online for installation specifics!
sudo apt-get install BeautifulSoup
sudo apt-get install nltk

Running the Parse_and_Find.py script will open up a GUI(uncomment line number 17 in Parse_and_Find.py) for nltk additional package downloads. Close the window after installing the packages. 
 
---------
WORKING:
---------
Please go throught the script to understand the detailed working. 

An ordered dict has been used for most of the working code. An ordered dict is the equivalent of a Linked Hash Map in Java. It is a resizable hash table that maintains the ordering of elements, based on the order in which they were inserted. 

Different parts of the html page are given different weights and the URL and title get more weight than the body of the page. This weight is used to determine how important the ocurrence of a word is in that respective place. 

A lemmatizer and a stop word remover have been implemented using the nltk module in python. A sample parse tree search to show how tags can be used to analyze the words with different weights has been shown. 

-----------
FUTURE WORK:
-----------

Although 48 hours were given, I was able to spend only 6 or so hours on the project. I've submitted the project within 24 hours, since I am travelling and may not be able to work on it further.  And hence there are a few things I tried to implement but couldn't and removed them from the final submission. Some of the future work is listed below:

1. The idea of using an Ordered dict was to detect "phrases" that ocurred together. This works by having a delta difference and checking if the number of ocurrences of the next word falls within delta and then printing them together. 

2. A more thorough distribution of weights and inclusion of more factors such as different levels of headers, image caption weightage, differentiating ads and bottom of page, differentiating the related/suggested posts etc. The project is never ending and it is possible to achieve much better results by including more factors and carefully experimenting with their weights. The current code is scalable to include all these. 

3. Wrapping up all the variables in a class and define the functions as methods. I wanted to do this, but figured the code as such was modular enough and didn't want to introduce classes for the sake of it. 

----------------------
WHAT DOESN'T WORK WELL
----------------------

Some of the keywords are still based on general words that occur so frequently, like "Privacy", "customers", "amazon" etc.

The weights can be experimented with to achieve good results in all these cases. 
