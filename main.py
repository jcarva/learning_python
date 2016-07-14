import threading
import time
import sys
from interface import *

COUNTDOWN = 5
lock = threading.Lock()

class Process(threading.Thread):

    def __init__(self, name):
        sys.stdout.write("Making thread name " + str(name) + "\n")
        sys.stdout.flush()
        threading.Thread.__init__(self)
        self.name = name
        self.countdown = COUNTDOWN

    def run(self):
        global lock
        #while True: ##Runnig in Loop
        lock.acquire()
        eval(self.name)(self.countdown, self.name)
        lock.release()
        time.sleep(1)


def main():
    for thread_name in functions:
        thread = Process(thread_name)
        thread.start()

if __name__ == '__main__':
    main()