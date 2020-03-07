import queue
from threading import Thread

from tweet2video import get_tweets

class VideoWorker(Thread):
    
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get work from the queue
            handles = self.queue.get()
            try:
                get_tweets(handles)
            finally:
                self.queue.task_done()

def main():
    # Create a queue to communicate with worker threads
    q = queue.Queue()
    handles = ["@NatGeo", "@REI"]
    # Create 4 worker threads
    for x in range(4):
        worker = VideoWorker(q)
        # Setting daemon to True will let the main 
        # thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    for handle in handles:
        q.put(handle)
    q.join()


    

if __name__ == '__main__':
    main()