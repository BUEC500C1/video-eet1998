import os
import tweepy as tw
import pandas as pd
import csv

# consumer keys and access tokens
consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'

# Twitter API authorization and initilization
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

def extract_tweets():
    tweets_list = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    tweets_list.extend(new_tweets)

    # id is updated to oldest tweet - 1 to keep track
    oldest_tweet = tweets_list[-1].id - 1
    print('...%s tweets have been downloaded so far' % len(tweets_list))

    # transforming the tweets into a 2D array that will be used to populate the csv

    outtweets = [[tweet.id_str, tweet.created_at,
    tweet.text.encode('utf-8')] for tweet in tweets_list]

# writing to the csv file

    with open(screen_name + '_tweets.csv', 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'created_at', 'text'])
        writer.writerows(outtweets)

if __name__ == '__main__':

    tweets_list(input("Enter the twitter handle of the person whose tweets you want to download: "))

