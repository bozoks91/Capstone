from twython import TwythonStreamer

APP_KEY = 'your appkey'
APP_SECRET = 'your app secret'
OAUTH_TOKEN = 'your token'
OAUTH_TOKEN_SECRET = 'your token secret'

outfile = '~/tweets.txt'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            fields = {'text', 'favorite_count', 'retweet_count','timestamp_ms', 'lang'}
            relevant_fields = {key:value for key,value in data.items() if key in fields}
            with open(outfile, 'a') as out:
                out.write(str(relevant_fields))

    def on_error(self, status_code, data):
        print status_code

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

search_terms = ['search_terms']

stream.statuses.filter(track=search_terms)