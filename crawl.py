""" File 'crawl.py' 
    assgn   : assignment 2/9
    tools   : -
    desc    : crawling instagram posts
    question: What countries use Instagram as online store?
"""
# IMPORT
import json
from instagram.client import InstagramAPI
from urllib import urlopen

# CONSTANT
# Register and get client_id here http://instagram.com/developer/
client_id = "c58899640d8943ccab8d1cacfaced36a"
base_url = "https://api.instagram.com/v1"
endpoints = "tags"
query = "onlineshopbali"
url = "{0}/{1}/{2}/media/recent?client_id={3}".format(base_url, endpoints, query, client_id)
count_caption = 0 # Intialize number of crawled captions

json_data = urlopen(url).read()
response = json.loads(json_data)

# Borrowed code from Danny's
# Write Instagram response to data_raw.txt
f = open('data_raw.txt', 'a+')
def write_to_txt(caption):
    if 'text' in caption:
        f.write(caption['id'] + '|')
        f.write(caption['created_time'] + '|')
        f.write(caption['from']['username'] + '|')

        text = caption['text'].replace('\n', ' ').replace('\r', ' ').encode('utf-8')
        f.write(text + '\n')

# Fetch next posts batch
def get_next_page(content):
    if 'pagination' in content:
        if 'next_url' in content['pagination']:
            return content['pagination']['next_url']
        else:
            return ''
    else:
        return ''

# MAIN
# Crawl posts from each page
while url != '':
	next_data = urlopen(url).read()
	response = json.loads(next_data)
	for i in range(0, len(response['data'])):
		if response['data'][i]['caption'] is not None:
			write_to_txt(response['data'][i]['caption'])
			count_caption += 1
	print 'crawled {0} captions from {1}'.format(count_caption, url)
	url = get_next_page(response)
            
f.close()
print "Successfully crawled {0}".format(count_caption)