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

def vid_url(statusid):
    try:
        status = api.get_status(statusid)
        variants = status.extended_entities['media'][0]["video_info"]["variants"]
        for i in variants:
            if i["content_type"]=='video/mp4':
                video_url= i["url"]
                break

        if video_url:
            return video_url.split('?')[0]
        else:
            return None
    except:
        return None
