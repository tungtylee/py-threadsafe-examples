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

class TSDict:
    def __init__(self):
        self.lock = Lock()
        self.objdict = {}
    def get(self, i):
        self.lock.acquire()
        if i not in self.objdict:
            self.objdict[i] = TSObj()
        self.lock.release()
        return self.objdict[i]
    def remove(self, i):
        self.lock.acquire()
        del self.objdict[i]
        self.lock.release()

# Functions
def myop(myobj):
    myobj.process()

def mydictop(mydict, i):
    myobj = mydict.get(i)
    myobj.process()


# Threading
mydict = TSDict()
mythreads = list()

for i in range(20):
    thread = Thread(target=mydictop, args=(mydict, i%5, ))
    mythreads.append(thread)

for i in range(20):
    mythreads[i].start()

for i in range(20):
    mythreads[i].join()

# Display
for k in mydict.objdict.keys():
    print(f"{k}:")
    myobj = mydict.get(k)
    myobj.display()


