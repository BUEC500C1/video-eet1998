import os
from queue import Queue
from threading import Thread
from time import time

class DownloadWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Do something
        try:
            # Do something
        finally:
            # Do something

def main():
    ts = time()
    # Do stuff
    # Create a queue to communicate with worker threads
    queue = Queue()
    # Create 4 worker threads
    for x in range(4):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main 
        # thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
        
