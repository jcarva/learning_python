import time
import sys

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
