import pyautogui
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

	def square( self ):
		pyautogui.moveTo(400, 400, duration = 1)
		pyautogui.moveTo(400, 600, duration = 1)
		pyautogui.moveTo(600, 600, duration = 1)
		pyautogui.moveTo(600, 400, duration = 1)
		pyautogui.moveTo(400, 400, duration = 1)