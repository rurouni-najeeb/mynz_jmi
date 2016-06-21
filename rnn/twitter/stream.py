import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListner(StreamListener):
    def on_data(self, data):
        try:
            with open('holi.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
consumer_key = 'g3FysYb4TCeYQJ1YYelj6U1DO'
consumer_secret = 'IgO90DNIClFcLezHVDmP0OviJaWNxKRvPRzLbYxxNdELVbxuRg'
access_token = '3246538160-cVmnEhoFRVTr9t9A4rNSHY5TmyLkBqmCCnMEHyf'
access_secret = 'dRZVP55wK38L0ab70tM2R1bErMutOwuU9zXA64CZiCkjS'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#api = tweepy.API(auth)

twitter_stream = Stream(auth,MyListner())
# make changes here
twitter_stream.filter(track=['#IndvsPak'])
