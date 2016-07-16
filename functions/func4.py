from func_base import FuncBase
import time
import sys

class Func4(FuncBase):
	def __init__(self, name, countdown):
		sys.stdout.write(" Create logic object " + str(name) + ", from func4 !\n")
		self.src_countdown = countdown
		self.countdown = countdown
		self.name = name
		self.setup_lock = 1

	def exe(self):

		if (self.setup_lock == 0):
			self.__main_logic()

		while (self.setup_lock == 1):
			self.__setup()

	def __setup(self):
		sys.stdout.write("Thread " + str(self.name) + " live and running in the setup mode!\n")

		self.progress_bar("Setup Progress " + str(self.name) + " :")
		load = raw_input("> Confirm Setup Loading(Y/n) : ")

		if (load == 'Y'):
			self.setup_lock = 0
			sys.stdout.write("Thread " + str(self.name) + " complete the setup mode!\n\n")
		elif (load == 'n'):
			sys.stdout.write("\nRetry Setup!\n\n")
		else:
			sys.stdout.write("Invalid option!\n")

	def __main_logic(self):
	    while (self.countdown):
	        time.sleep(0.3)
	        sys.stdout.write("Thread " + str(self.name) + " (" + str(self.countdown) + ")\n")
	        sys.stdout.flush()
	        self.countdown -= 1

	    self.countdown = self.src_countdown
	    self.__alert()

	def __alert(self):
		sys.stdout.write("Internal contdown restarted !\n\n")