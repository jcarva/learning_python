from func_base import FuncBase
import time
import sys
import requests

class Func1(FuncBase):
	def __init__(self, name, countdown):
		sys.stdout.write(" Create logic object " + str(name) + ", from func1 !\n")
		self.src_countdown = countdown
		self.countdown = countdown
		self.name = name
		self.setup_lock = 1 #lock to able setup mode

	def exe(self):
		if (self.setup_lock == 0):
			self.__main_logic()
		else:
			while (self.setup_lock == 1):
				self.__setup()

	def __setup(self):
		sys.stdout.write("\n\nThread " + str(self.name) + " live and running in the setup mode!\n")

		self.progress_bar(" Setup Progress " + str(self.name) + " :")
		load = raw_input(" > Confirm Setup Loading(Y/n) or Cancel Setup(C): ")

		if (load == 'Y'):
			self.setup_lock = 0
			sys.stdout.write("Thread " + str(self.name) + " complete the setup mode!")
		elif (load == 'n'):
			sys.stdout.write("\nRetry Setup!")
		elif (load == 'C'):
			self.setup_lock = 0
			sys.stdout.write("\nThank you!")
		else:
			sys.stdout.write("\nInvalid option!")

	def __main_logic(self):
	    sys.stdout.write("\n\nThread " + str(self.name) + " executing the main logic!\n")
	    req = requests.get('http://www.w3schools.com/website/Customers_MYSQL.php')
	    data = req.json()[0]
	    while (self.countdown):
	        time.sleep(0.3)
	        sys.stdout.write(" Thread " + str(self.name) + " (" + str(self.countdown) + ")\n")
	        print (data)
	        sys.stdout.flush()
	        self.countdown -= 1

	    self.countdown = self.src_countdown
	    self.__alert()
	    sys.stdout.write("Thread " + str(self.name) + " complete the main logic!")

	def __alert(self):
		sys.stdout.write("\n Internal contdown restarted !\n")