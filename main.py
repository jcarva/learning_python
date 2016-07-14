import pyautogui
import time
import threading
import sys

functions = ['func1', 'func2', 'func3', 'func4']

COUNTDOWN = 5
lock = threading.Lock()

def func1(countdown, name):
    while (countdown):
        time.sleep(0.3)
        sys.stdout.write("Thread " + str(name) + " (" + str(countdown) + ")\n")
        sys.stdout.flush()
        countdown -= 1

def func2(countdown, name):
    while (countdown):
        time.sleep(0.3)
        sys.stdout.write("Thread " + str(name) + " (" + str(countdown) + ")\n")
        sys.stdout.flush()
        countdown -= 1

def func3(countdown, name):
    while (countdown):
        time.sleep(0.3)
        sys.stdout.write("Thread " + str(name) + " (" + str(countdown) + ")\n")
        sys.stdout.flush()
        countdown -= 1

def func4(countdown, name):
    while (countdown):
        time.sleep(0.3)
        sys.stdout.write("Thread " + str(name) + " (" + str(countdown) + ")\n")
        sys.stdout.flush()
        countdown -= 1


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

for thread_name in functions:
    thread = Process(thread_name)
    thread.start()