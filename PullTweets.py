# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:15:48 2015

@author: Bozoks91
"""

import time
from collections import Counter
from twython import TwythonStreamer
# appending data to a global variable is pretty poor form
# but it makes the example much simpler
tweets = []

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""
    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python dict representing a tweet"""
        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)
            print ("received tweet #", len(tweets))
        # stop when we've collected enough
        if len(tweets) >= 100:
            self.disconnect()
            print("Time number threshold of number of tweets is reached: ",len(tweets))
            
        # stop when amount of time you want to collect data is reached in seconds
        if int(time.time()-start)>=100:
            self.disconnect()
            print("Time elaspsed is: ",int(time.time()-start), "seconds")
          
    def on_error(self, status_code, data):
        print (status_code, data)
        self.disconnect()

start = time.time()
stream = MyStreamer('APP_KEY', 'APP_SECRET','OAUTH_TOKEN', 'OAUTH_TOKEN_SECRET')

# starts pulling data that about contain the key words mentioned in list t
t = ["Lebron","Trump"]
stream.statuses.filter(track=t)

# if instead we wanted to start consuming a sample of *all* public statuses
# stream.statuses.sample()



#top_hashtags = Counter(hashtag['text'].lower()
#for tweet in tweets
#for hashtag in tweet["entities"]["hashtags"])
#print (top_hashtags.most_common(5))
#


