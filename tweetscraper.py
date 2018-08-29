from TwitterAPI import TwitterAPI;
import json;

SEARCH_TERM = 'geertwilderspvv'

r = api.request('statuses/user_timeline', {'screen_name': SEARCH_TERM, 'count': 3200})

with open('geert.json', 'w') as outfile

for item in r:
    json.dump(item if 'text' in item else item, outfile)
    // print(item if 'text' in item else item)

print('\nQUOTA: %s' % r.get_quota())