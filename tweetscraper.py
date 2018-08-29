from TwitterAPI import TwitterAPI
import json
import configparser

def getTweets(SEARCH_TERM):

	config = configparser.RawConfigParser()
	config.read('config.ini')

	# SEARCH_TERM = 'geertwilderspvv'

	api = TwitterAPI(config.get('DEFAULT', 'api_key'),
	                 config.get('DEFAULT', 'api_secret_key'),
	                 config.get('DEFAULT', 'access_token'),
	                 config.get('DEFAULT', 'access_token_secret'))

	tweets = []

	for page in range(1):

		r = api.request('statuses/user_timeline', {'screen_name': SEARCH_TERM, 'count': 200, 'page' : page + 1})

		for item in r:
			tweet = {}
			tweet['id'] = item['id']
			tweet['created_at'] = item['created_at']
			tweet['text'] = item['text']
			tweets.append(tweet)

	# print(len(tweets))

	collection = json.dumps({ 'member': SEARCH_TERM, 'tweets': tweets})

	with open('tweetcollection/' + SEARCH_TERM + '.json', 'w') as outfile:
		json.dump(json.loads(collection), outfile)
