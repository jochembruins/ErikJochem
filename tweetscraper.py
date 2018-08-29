from TwitterAPI import TwitterAPI
import json
import configparser

config = configparser.RawConfigParser()
config.read('config.ini')

SEARCH_TERM = 'geertwilderspvv'

api = TwitterAPI(config.get('DEFAULT', 'api_key'),
                 config.get('DEFAULT', 'api_secret_key'),
                 config.get('DEFAULT', 'access_token'),
                 config.get('DEFAULT', 'access_token_secret'))

r = api.request('statuses/user_timeline', {'screen_name': SEARCH_TERM, 'count': 3200})

tweets = []

for item in r:
	tweets.append(item)

with open('geert.json', 'w') as outfile:
    json.dump(tweets, outfile)

# print('\nQUOTA: %s' % r.get_quota())
