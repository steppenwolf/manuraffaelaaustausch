#! /usr/bin/python
# -*- coding: utf-8 -*-

class Knuddel(object):
	def __init__(self, name):
		self.name = name
		self.freunde = set()
	def vorstellung(self):
		print "Hallo, ich bin ein Knuddel und mein Name ist", self.name, "."
	def begruessen(self, knuddel):
		self.vorstellung()
		knuddel.vorstellung()
		self.freunde.add(knuddel)
		knuddel.freunde.add(self)
	def knuddeln(self, knuddel):
		if self in knuddel.freunde and knuddel in self.freunde:
			print self.name, "und", knuddel.name, "haben sich ganz arg lieb."
		else:
			print "Bitte seien Sie nicht so zudringlich."
			raise StandardError
