import logging
import threading
from time import sleep
from threading import *
import time


import yaml
from yaml.loader import SafeLoader

logging.basicConfig(filename='concurrent.log',level=logging.DEBUG,
                    format='%(asctime)s %(message)s')


def First(lock):
    for i in range(5):
        lock.acquire()
        logging.debug("first")
        lock.release()


lock =threading.Lock()

# concurrent objects
t1 = threading.Thread(target=First, args=(lock,))
t2 = threading.Thread(target=First,args=(lock,))


# concurrent starts
t1.start()
t2.start()

t1.join()
t2.join()

print(" finish")