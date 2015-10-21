from collections import defaultdict

class hello(object):
	__slots__=['dict_', 'a']
	def __init__(self, dict_, a):
		self.dict_= dict_
		self.a =a
	def printobject(self):
		print self.dict_
		print self.a
dict_={}
for x in range(10):
	dict_[x]=x**2
obj1 = hello(dict_,4)
obj1.printobject()