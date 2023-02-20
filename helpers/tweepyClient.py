import tweepy

def getTweepyClient(bearer_token):
    return tweepy.Client(bearer_token)
