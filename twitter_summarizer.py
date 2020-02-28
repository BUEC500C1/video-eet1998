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

def create_directories():
    image_dir_name = 'ImagesDirectory'
    video_dir_name = 'VideoDirectory'
    if not os.path.exists(image_dir_name):
        os.mkdir(image_dir_name)
        print("Images directory created.")
    else:
        print("Images directory already exists.")

    if not os.path.exists(video_dir_name):
        os.mkdir(video_dir_name)
        print("Video directory created.")
    else:
        print("Video directory already exists.")

def get_tweets(handle):
    #num_tweets = 10
    tweets = api.user_timeline(screen_name=handle)
    array = []
    tweets_for_images = [tweet.text for tweet in tweets]
    for i in tweets_for_images:
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
        image.save(path + file_name)
        file_num += 1

def image2video():




if __name__ == '__main__':
    get_tweets("NatGeo")


