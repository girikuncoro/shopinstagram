""" File 'cleaner.py' 
    assgn   : assignment 2/9
    tools   : -
    desc    : cleaning raw data from unrelated stuffs
    question: What countries use Instagram as online store?
"""
# IMPORT
import re
import datetime

# Clean raw_data.txt, remove hashtags, smiley, multiple spaces, links
# Rewrite to data_cleaned.txt
f_raw = open('data_raw.txt', 'r')
f_cleaned = open('data_cleaned.txt', 'w')
for line in f_raw.readlines():
    cap_array = line.split('|')
    cap_id = cap_array[0]
    cap_time = datetime.datetime.fromtimestamp(int(cap_array[1])).strftime('%Y-%m-%d')
    cap_user = cap_array[2]  
    cap_text = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", cap_array[3]).lower() # Removing hashtags
    cap_text = ''.join([i for i in cap_text if not i.isdigit()]) # Removing numbers
    cap_text = re.sub(' +',' ',cap_text) # Removing multiple spaces
    f_cleaned.write(cap_id + '|' + cap_time + '|' + cap_user + '|' + cap_text + '\n')
f_cleaned.close()
f_raw.close()