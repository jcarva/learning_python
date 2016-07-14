import pyautogui
import threading
import time
import sys

"""Describe which functions we'll use"""
from frank import func1, func2, func3, func4
functions = ['func1', 'func2', 'func3', 'func4']

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

        # while True: #Running in Loop
        lock.acquire()
        eval(self.name)(self.countdown, self.name)
        lock.release()


def main():
    for thread_name in functions:
        thread = Process(thread_name)
        thread.start()

if __name__ == '__main__':
    main()