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
stream = MyStreamer('PtFW0bLiVACNukYITt0UjyvOc', 'j6T8eTigXbdcVNVWbVYvGHgc5OyuqyFOeItbTV4rzaf542Y8ZK',
'3959083463-N6uSuV7D0TBUIGCOl2cll8O5x9fUI3NvOULMHxJ', 'KX6RP9X6fcZX9PGrWNectpeBmUzFwCi4WKcxr8UudgIi0')

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


