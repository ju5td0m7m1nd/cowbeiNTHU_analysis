import os
import requests
import json
import codecs
import jieba
import pickle

TOKEN = os.environ['TOKEN']

COMMENT_URL = 'https://graph.facebook.com/v2.8/'
OBJECT_ID = '576472312465910'
QUERY = '/feed?fields=message,comments.limit(2000).summary(true){comments,message,from,message_tags},reactions.limit(2000).summary(true),shares,created_time,story&access_token='

data = []

posts = []
comments = []
res = requests.get(COMMENT_URL + OBJECT_ID +QUERY+TOKEN)
corpus = []
res_json = json.loads(res.text)
page = 0
data.append(res_json['data'])

while 'next' in res_json['paging']:
  print (res_json['paging']['next'])
  res = requests.get(res_json['paging']['next']) 
  res_json = json.loads(res.text)
  data.append(res_json['data'])
  if res_json['data'][0]['created_time'].split('-')[0] != str(2017):
    break

with open('feed.pickle','w') as f:
    pickle.dump(data,f)
