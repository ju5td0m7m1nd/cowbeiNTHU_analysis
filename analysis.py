import pickle
import operator

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
  print (sorted_users[:10])

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
  print (sorted_users[:10])

  
if __name__ == '__main__':
  most_frequent_reactor(feeds)
  most_frequent_reply(feeds)
