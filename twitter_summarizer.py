import os
import queue
from threading import Thread
from time import time
import multiprocessing
import tweepy
import configparser
import ffmpeg
import glob
import PIL as pillow
from PIL import Image, ImageDraw, ImageFont


class VideoWorker(Thread):

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

    def __init__(self, path, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get work from the queue
            task = self.queue.get()
            try:
                get_tweets(task)
            finally:
                self.queue.task_done()

    def get_tweets(self, handle):
        tweets = []
        tweets_new = api.user_timeline(screen_name = handle, count = 10)
        tweets.extend(tweets_new)
        num = 0
        #tweets_for_images = [tweet.text for tweet in tweets]
        for status in tweets:
            text_only = status.text
            tweet2image(text_only, handle, num)
            num += 1

    def tweet2image(self, text_only, handle, num):
        if not os.path.isdir(handle + '_tweets'):
            os.mkdir(handle + '_tweets')
        
        file_num = 1
        file_name = ""
        i = 0
        while i < len(text_only):
            file_name = handle + '_tweets/' + handle + '_img_' + str(file_num) + '.png'
            image = Image.new(mode="RGB", size=(200,70))
            draw = ImageDraw.Draw(image)
            draw.text((10,10), text_only.encode('cp1252', 'ignore'), fill=(0,0,0))
            image.save(file_name)
            file_num += 1
        return self.image2video(handle)

    def image2video(self, handle):
        if not os.path.isdir('VideoWorker'):
            os.mkdir('VideoWorker')
        fileName = os.getcwd() + '/' + handle + '_tweets/' + '.png'
        videoName = 'VideoWorker/' + handle + '.mp4'
        ffmpeg.input(fileName, pattern_type = 'glob', framerate = 0.3).output(videoName).run()

def main():
    ts = time()
    # Do stuff
    # Create a queue to communicate with worker threads
    queue = Queue()
    # Create 4 worker threads
    for x in range(4):
        worker = VideoWorker(queue)
        # Setting daemon to True will let the main 
        # thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()

if __name__ == '__main__':
    main()



