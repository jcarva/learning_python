import time
import sys
from func1 import Func1
from func2 import Func2
from func3 import Func3
from func4 import Func4

"""Describe which functions we'll use"""
functions = ['func1', 'func2', 'func3', 'func4']



"""Declare which functions we'll use"""

def func1(countdown, name):
	func1 = Func1(countdown, name)
	func1.exe()

def func2(countdown, name):
	func2 = Func2(countdown, name)
	func2.exe()

def func3(countdown, name):
	func3 = Func3(countdown, name)
	func3.exe()

def func4(countdown, name):
	func4 = Func4(countdown, name)
	func4.exe()
