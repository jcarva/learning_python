from func_base import FuncBase
import time
import sys

class Func2(FuncBase):
	def __init__(self, countdown, name):
		self.countdown = countdown
		self.name = name

	def exe(self):
	    while (self.countdown):
	        time.sleep(0.3)
	        sys.stdout.write("Thread " + str(self.name) + " (" + str(self.countdown) + ")\n")
	        sys.stdout.flush()
	        self.countdown -= 1

	    self.__alert2()

	def __alert2(self):
		sys.stdout.write("Thread " + str(self.name) + " Done !\n")