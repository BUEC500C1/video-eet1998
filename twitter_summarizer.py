import os
#import pandas as pd
import csv
import threading
import tweepy
import PIL as pillow
from PIL import Image, ImageDraw, ImageFont

# consumer keys and access tokens
consumer_key = 'Ij5a4mBmBvNp4aiZ7F8uPhAWi'
consumer_secret = 'DtrH2IGyq6KMds9zXzvsefd2knSee7K9xKqOdchvtTGuphCP2z'
access_token = '931158103831216128-T4nbPvu1irazZ0t49MkZZqjT2xmQDSP'
access_token_secret = 'y7WQZkM9jsiuQtmpopOc7rNctN910utOE3gDzyJaMYIgX'

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

def tweet2image(array):
    file_num = 1
    file_name = ""
    for i in array:
        file_name = 'img_' + str(file_num) + '.png'
        fnt = ImageFont.truetype('arial.ttf', 15)
        image = Image.new(mode="RGB", size=(200,70), color="red")
        draw = ImageDraw.Draw(image)
        draw.text((10,10), str(i), font=fnt, fill=(255,255,0))
        image.save(file_name)
        os.system(file_name)
        file_num += 1



if __name__ == '__main__':
    get_tweets("NatGeo")


