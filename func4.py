import time
import sys

class Func4:
	def __init__(self, countdown, name):
		self.countdown = countdown
		self.name = name

	def exe( self ):
	    while (self.countdown):
	        time.sleep(0.3)
	        sys.stdout.write("Thread " + str(self.name) + " (" + str(self.countdown) + ")\n")
	        sys.stdout.flush()
	        self.countdown -= 1