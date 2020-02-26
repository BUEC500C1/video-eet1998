import os
import tweepy
import pandas as pd
import csv
import threading

# consumer keys and access tokens
consumer_key = 'yourkeyhere'
consumer_secret = 'yourkeyhere'
access_token = 'yourkeyhere'
access_token_secret = 'yourkeyhere'

# Twitter API authorization and initilization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_tweets(handle):
    #num_tweets = 10
    tweets = api.user_timeline(screen_name=handle)
    array = []
    tweets_for_csv = [tweet.text for tweet in tweets]
    for i in tweets_for_csv:
        array.append(i)
    print(array)

if __name__ == '__main__':
    get_tweets("twitter-handle")


