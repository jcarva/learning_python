import pyautogui
import time
import sys

class Func2:
	def __init__(self, countdown, name):
		self.countdown = countdown
		self.name = name

	def exe( self ):
	    while (self.countdown):
	        time.sleep(0.3)
	        sys.stdout.write("Thread " + str(self.name) + " (" + str(self.countdown) + ")\n")
	        sys.stdout.flush()
	        self.countdown -= 1

	def square( self ):
		pyautogui.moveTo(800, 400, duration = 1)
		pyautogui.moveTo(1000, 400, duration = 1)
		pyautogui.moveTo(1000, 600, duration = 1)
		pyautogui.moveTo(800, 600, duration = 1)
		pyautogui.moveTo(800, 400, duration = 1)