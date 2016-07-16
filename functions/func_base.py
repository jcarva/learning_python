from abc import ABCMeta, abstractmethod
import sys
import time
import random

class FuncBase:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def exe(self):
		pass

	def progress_bar(self, prefix):
		for i in self.print_progess(range(100), prefix, "% Complete", 30):
			time.sleep(random.uniform(0.01, 0.09)) # long computation

	def print_progess(self, it, prefix, suffix , size):
	    count = len(it)
	    chr_bar = '#'
	    def _show(_i):
	        x = int(size*_i/count)
	        sys.stdout.write("%s[%s%s] %i%s\r" % (prefix, chr_bar*x, "."*(size-x), _i, suffix))
	        sys.stdout.flush()

	    _show(0)
	    for i, item in enumerate(it):
	        yield item
	        _show(i+1)
	    sys.stdout.write("\n")
	    sys.stdout.flush()