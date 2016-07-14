from abc import ABCMeta, abstractmethod

class FuncBase:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def exe(self):
		pass