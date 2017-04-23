import pickle
import operator
import jieba.analyse

readFile = pickle.load( open('feed.pickle', 'rb'))
feeds = []
[ feeds.append(mess) for messages in readFile for mess in messages]


def most_frequent_reactor(feeds):
  users = {} 
  for i in range(0, len(feeds)):
    if 'reactions' in feeds[i]:
      for u in feeds[i]['reactions']['data']:
        if u['name'] in users:
          users[u['name']] += 1
        else:
          users[u['name']] = 1
  sorted_users = sorted(users.items(), key=operator.itemgetter(1), reverse=True)
  print (sorted_users[:20])

def most_frequent_reply(feeds):
  users = {}
  for i in range(0, len(feeds)):
    if 'comments' in feeds[i]:
      for u in feeds[i]['comments']['data']:
        user = u['from']['name']
        if user in users:
          users[user] += 1
        else:
          users[user] = 1
  sorted_users = sorted(users.items(), key=operator.itemgetter(1), reverse=True)
  print (sorted_users[:20])

def remove_prefix(message):
  if '靠北清大' in message:
    message = message.split('\n', 1)[1] 
  if '投稿日期' in message:
    message = message.split('投稿日期')[0]
  message=message.split('Submitted')[0]
  return message


def most_frequent_words(feeds, month):
  words = {} 
  for i in range(0, len(feeds)):
    if 'message' in feeds[i]:
      if len(month) < 2:      
        month = '0' + str(month)
      if '2017-'+month in feeds[i]['created_time']:
        feed = remove_prefix(feeds[i]['message'])
        keywords = jieba.analyse.extract_tags(feed, topK=20)
        for keyword in keywords:
          if keyword in words :
            words[keyword] += 1
          else:
            words[keyword] = 1
  sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
  return sorted_words 
if __name__ == '__main__':
  for i in range(0, 30):
    print (feeds[i]['reactions'])
  #most_frequent_reactor(feeds)
  #most_frequent_reply(feeds)
  #print(most_frequent_words(feeds, '1')[:40])
  #print(most_frequent_words(feeds, '2')[:40])
  #print(most_frequent_words(feeds, '3')[:40])
