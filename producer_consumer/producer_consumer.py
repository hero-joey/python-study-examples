import random
import time
from queue import Queue
from threading import Thread


class Producer(Thread):
    def __init__(self, produce_queue):
        super().__init__()
        self.queue = produce_queue

    def run(self):
        while True:
            a = random.randint(0, 10)
            b = random.randint(90, 100)
            print("produce %d, %d" % (a, b))
            self.queue.put((a, b))
            time.sleep(2)


class Consumer(Thread):
    def __init__(self, consume_queue):
        super().__init__()
        self.queue = consume_queue

    def run(self):
        while True:
            number_tuple = self.queue.get(False)
            total = sum(number_tuple)
            print("elements: %s, sum:%d" % (number_tuple, total))
            time.sleep(random.randint(0, 10))


queue = Queue()
producer = Producer(queue)
consumer = Consumer(queue)
producer.start()
consumer.start()
producer.join()
consumer.join()
