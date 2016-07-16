import threading
import time
import sys
from interface import *

lock = threading.Lock()

class Process(threading.Thread):

    def __init__(self, name, logic_object):
        sys.stdout.write("Building thread " + str(name) + "\n")
        sys.stdout.flush()
        threading.Thread.__init__(self)
        self.logic_object = logic_object

    def run(self):
        time.sleep(len(projects) * 0.125) # sync initial console message
        global lock
        #while True: ##Runnig in Loop
        for x in xrange(3):
            lock.acquire()
            self.logic_object.exe()
            lock.release()
            time.sleep(2)


def main():
    x = 1
    for thread_logic in projects:
        thread = Process(x, thread_logic)
        thread.start()
        x+= 1

if __name__ == '__main__':
    main()
