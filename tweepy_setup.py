import tweepy

twitter_keys = {
        'consumer_key':        'your_consumer_key',
        'consumer_secret':     'your_consumer_secret',
        'access_token_key':    'your_access_token_key',
        'access_token_secret': 'your_access_token_secret'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)


# Call twitter API to get tweet 

status = api.get_status("statusid")
