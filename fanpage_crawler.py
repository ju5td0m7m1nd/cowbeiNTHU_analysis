import os
import requests
import json
import codecs
import jieba
import pickle

print os.environ
LIMIT = 25
TOKEN = os.environ['TOKEN']
COMMENT_URL = 'https://graph.facebook.com/v2.8/'
OBJECT_ID = '576472312465910'
QUERY = '/feed?fields=message,comments.limit('+str(LIMIT)+').summary(true){comments,message,from,message_tags},reactions.limit('+str(LIMIT)+').summary(true),shares,created_time,story&access_token='

data = []

posts = []
comments = []
res = requests.get(COMMENT_URL + OBJECT_ID +QUERY+TOKEN)
corpus = []
res_json = json.loads(res.text)
page = 0
data.append(res_json['data'])

try:
  while 'next' in res_json['paging']:
    #print (res_json['paging']['next'])
    res = requests.get(res_json['paging']['next']) 
    res_json = json.loads(res.text)
    if 'data' in res_json:
      data.append(res_json['data'])
      print '.'
    else:
      print res_json
except:
  with open('feed.pickle','w') as f:
      pickle.dump(data,f)
