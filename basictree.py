#! /usr/bin/python
# -*- coding: utf-8 -*-

class Baum(object):
	def __init__(self, name=""):
		self.blaetter = []
		self.wurzel = None
		self.name = name
	def __str__(self):
		if self.name:
			return self.name
		else:
			return object.__str__(self)

if __name__ == "__main__":
	a = Baum("a")
	aa = Baum("aa")
	ab = Baum("ab")

	#konsistent
	aa.wurzel = a
	#inkonsistent!
	a.blaetter = [aa]
	#konsistent

	print aa
