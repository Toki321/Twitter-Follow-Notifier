import tweepy
import os
import dotenv

dotenv.load_dotenv()

def getTweepyClient(number):
    bearer_token = "BEARER_TOKEN_" + str(number)
    bearer_token = os.getenv(bearer_token)
    return tweepy.Client(bearer_token)



