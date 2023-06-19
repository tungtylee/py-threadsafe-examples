from threading import Thread
from threading import Lock
import numpy as np
import time

# Class
class TSObj:
    def __init__(self):
        self.lock = Lock()
        self.waitTime = []
        self.processTime = []
    def process(self):
        s = time.time()
        self.lock.acquire()
        e = time.time()
        self.waitTime.append(e-s)
        pt = np.random.rand()*10
        time.sleep(pt)
        self.processTime.append(pt)
        self.lock.release()
    def display(self):
        self.lock.acquire()
        for w, p in zip(self.waitTime, self.processTime):
            print(f"{w:.2f} {p:.2f}")
        self.lock.release()

# Functions
def myop(obj):
    obj.process()

# Threading
myobj = TSObj()
mythreads = list()

for i in range(10):
    thread = Thread(target=myop, args=(myobj,))
    mythreads.append(thread)

for i in range(10):
    mythreads[i].start()

for i in range(10):
    mythreads[i].join()

# Display
myobj.display()


