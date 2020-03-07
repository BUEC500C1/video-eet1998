import os
import tweepy
import configparser
import ffmpeg
import glob
import PIL as pillow
from PIL import Image, ImageDraw, ImageFont


'''
config = configparser.ConfigParser()
config.read('keys')
consumer_key = config.get('auth','consumer_key').strip()
consumer_secret = config.get('auth','consumer_secret').strip()
access_key = config.get('auth','access_token').strip()
access_secret = config.get('auth','access_secret').strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
'''

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
    tweets = []
    tweets_new = api.user_timeline(screen_name = handle, count=10)
    tweets.extend(tweets_new)
    num = 1
    for status in tweets:
        text_only = status.text
        tweet2image(text_only, handle, num)
        num += 1

    def tweet2image(text_only, handle, num):
        if not os.path.isdir(handle + '_tweets'):
            os.mkdir(handle + '_tweets')
        file_name = handle + '_tweets/' + handle + '_img_' + str(num) + '.png'
        font = ImageFont.truetype("Arial.ttf", 15)
        image = Image.new('RGB', (203, 350), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text((20,220), text_only, font = font, fill = (0,0,0))
        image.save(file_name)


    def image2video(handle):
        if not os.path.isdir(handle + '_video'):
            os.mkdir(handle + '_video')
        file_name = os.getcwd() + '/' + handle + '_tweets/' + '.png'
        video_name = 'video/' + handle + '.mp4'
        ffmpeg.input(file_name, pattern_type = 'glob', framerate = 0.3).output(video_name).run()    