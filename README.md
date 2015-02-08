## About
The goal of this project is to find out which countries use Instagram as online stores the most. We will also collect Instagram posts that correspond to onlineshop tags for further analyses on what kinds of products are sold by the online shop members.

## Requirement
This project uses Instagram API and NLTK library for Natural Language Processing. In the script, I already assigned client id as permission to use Instagram API, you don't have to generate by yourself. Install Python and NLTK if you haven't.

1. Python 2.7 (https://www.python.org/downloads/), do not use Python 3 as not supported by NLTK library
2. NLTK (http://www.nltk.org/install.html)

REQUIREMENT
1. Python - I used Python 2.7, and some things:
	a. Request - To do HTTP request. Install pip first, and then type 'pip install request' in terminal/cmd. (http://docs.python-requests.org/en/latest/). There is a good tutorial for this module in (http://nbviewer.ipython.org/github/ptwobrussell/mining-the-social-web-2nd-edition/blob/master/ipynb/Chapter%202%20-%20Mining%20Facebook.ipynb)
	b. Numpy - Python package for scientific computing (http://www.numpy.org/) I only provide the Win-version installer
2. NLTK - Python based library for language analysis (http://www.nltk.org/) I only provide the Win-version installer

HOW-TO
1. To crawl and store data from the Big Red Confessions' Page, run the "crawler.py"; it will generate "data_raw.txt" file
2. To do text processing (removing punctuation, stop words, stemming, and other cleaning) from the data_raw.txt, run the "crawler.py". It will generate "data_cleaned.txt" file
3. To analyze the data from data_cleaned.txt, run the "analyzer.py". It takes ~5 minutes to see the result.
	a. The long run is caused by the language analysis part, if you want to take a quick look for the result, just comment these 2 lines:
		- annotated_msg = pos_tagging( msg_dict[msg_id] ) in line 55
		- if (word in annotated_msg and annotated_msg[word] in nouns): in line 59
	b. The most commented and liked lists will only show the <ID> of confessions. To check the confession message, open "data_raw.txt" and search for the #<ID>

## How To

1. To learn how many posts in Instagram related to online stores, run "country_shopper.py", it will print out total number of posts, related tags and most active countries.
2. To learn what kind of products are sold in Instagram (onlineshopbali tag), run "crawl.py", it will generate "data_raw.txt" with more than 20,000 posts. I chose Bali due to frequent use of english words.
3. To clean the data, run "cleaner.py", it will remove unnecessary stuffs like smiley, hashtags, unrelated links, etc and generate "data_cleaned.txt"
4. Data analyses is postponed due to limited amount of time. I will update this project again after learning some analyses techniques.

## Author

Hello, I'm Giri! This project is written by me as part of my assignment in INFO6010 - Computational Method in Information Science. DanCo (http://www.cs.cornell.edu/~danco/) teaches this, he is a great professor! Checkout my web (http://kuncoro.co) to know more about me.
