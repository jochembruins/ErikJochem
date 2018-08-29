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

# with open('geert.json', 'w') as outfile

for item in r:
    # json.dump(item if 'text' in item else item, outfile)
    print(item if 'text' in item else item)

# print('\nQUOTA: %s' % r.get_quota())
