import tweepy
import json

#Token Dictionary
twitter_keys = {
        'consumer_key':        'FIBi6KPFLz3TiQIcpt8h0WTPg',
        'consumer_secret':     'v8BuMxO8wmw9eDm8KMhCBeGYCBESSt6LFL0FDMWvgx0HvTEANj',
        'access_token_key':    '489702600-bePq9hG3i9yg8ucKQDNwLDXi66Klb1flDpNA4Nqa',
        'access_token_secret': 'NLvNYumTsDzgckeLyjsxlUTh67i1jrAwu0t699rWUpKLx'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

#Make call on home timeline, print each tweets text
public_tweets = api.home_timeline()

#Format Tweets with JSON
tweet_to_json = public_tweets[0]
json_str = json.dumps(tweet_to_json._json)

#deserialise string into python object and then save ouput 
parsed = json.loads(json_str)
with open('./data/tweet1.json', 'w') as f:
    json.dump(parsed, f)