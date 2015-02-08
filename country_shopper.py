""" File 'country_shopper.py' 
    assgn   : assignment 2/9
    tools   : -
    desc    : count most active countries doing onlineshop posts
    question: What countries use Instagram as online store?
"""
# IMPORT
import json
from instagram.client import InstagramAPI
from pprint import pprint
from urllib import urlopen

# CONSTANT
# Register and get client_id here http://instagram.com/developer/
client_id = "83929ff39a334b7f9e40417e871c548f"
base_url = "https://api.instagram.com/v1"
endpoints = "tags"
query = "onlineshop" # Find onlineshop related tags in Instagram
url = "{0}/{1}/search?q={2}&client_id={3}".format(base_url, endpoints, query, client_id)

count_total = 0

# Count number of posts related to onlineshop tag
for i in range(0, len(response['data'])):
    count_total += int(response['data'][i]['media_count'])

print count_total

# Online shops tag with number of posts
for i in range(0, len(response['data'])):
    print response['data'][i]['name'], response['data'][i]['media_count']

# Filter 'onlineshop' to group countries
shopper = {}
for i in range(0, len(response['data'])):
    shopper[response['data'][i]['name'][10:]] = int(response['data'][i]['media_count'])

# Group countries dictionary
count_countries = {"indonesia": 0, "malaysia": 0, "philippines": 0, "hongkong": 0, "unknown": 0}
countries = {}
countries["indonesia"] = ["indo", "indonesia", "murah", "jakarta", "id", "jkt", "surabaya", 
                        "terpercaya", "sby", "malang", "bali", "jogja", "solo", "semarang", 
                        "_indo", "hijab", "batam", "baju", "ind", "tas", "sepatu", "palembang", 
                        "denpasar", "samarinda", "medan", "bandung"]
countries["malaysia"] = ["pingmalaysia", "pingmy", "malaysia"]
countries["philippines"] = ["pingph", "perph", "pingphilippines", "philippines", "pingmanila", 
                            "mnl", "cebu", "manila", "ph"]
countries["hongkong"] = ["hk"]
countries["unknown"] = ["", "trusted", "instagram", "pping", "pe", "sph", "ing", "ping", "per", "pers", "s"]

# Count posts from countries
for country in countries:
    for word in countries[country]:
        for i in range(0, len(shopper)):
            if shopper.keys()[i] == word:
                count_countries[country] += shopper[word]

pprint(count_countries)