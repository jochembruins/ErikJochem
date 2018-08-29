from tweetscraper import getTweets
import json

with open('TweedeKamerScraper/leden_complete.json', 'r') as json_file:
	data = json.load(json_file)

for members in data:
	if 'twitter' in members:
		print('lol')
		try:
			getTweets(members['twitter'].replace('https://twitter.com/', ''))
		except:
			print('no tweets for: ' + members['twitter'])

