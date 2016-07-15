from abc import ABCMeta, abstractmethod
import sys
import time

class FuncBase:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def exe(self):
		pass

	def progress_bar(self, initial_message, final_message):
		prefix = initial_message
		suffix = final_message
		items = list(range(0, 100))
		i = 0
		l = len(items)

		# Initial call to print 0% progress
		self.print_progress(i, l, prefix , suffix , barLength = 50)
		for item in items:
		    # Do stuff...
		    time.sleep(0.05)
		    # Update Progress Bar
		    i += 1
		    self.print_progress(i, l, prefix , suffix , barLength = 50)

	def print_progress (self, iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
	    filledLength    = int(round(barLength * iteration / float(total)))
	    percents        = round(100.00 * (iteration / float(total)), decimals)
	    bar             = '@' * filledLength + '-' * (barLength - filledLength)
	    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
	    sys.stdout.flush()
	    if iteration == total:
	        sys.stdout.write('\n')
	        sys.stdout.flush()