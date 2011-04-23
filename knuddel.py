#! /usr/bin/python
# -*- coding: utf-8 -*-

class KnuddelError(StandardError):
	pass

class KnuddelName(KnuddelError):
	pass

class BabyName(KnuddelName):
	pass



class Knuddel(object):
	def __init__(self, name=None):
		if not name == None:
			self.name = name
		self.freunde = set()
	def vorstellung(self):
		try:
			print "Hallo, ich bin ein Knuddel und mein Name ist", self.name, "."
		except AttributeError:
			raise BabyName("Das Baby hat noch keinen Namen. Bevor es sich vorstellen kann, muss die Funktion 'benennen()' aufgerufen werden")
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
			raise KnuddelError
	def __add__(self, knuddel):
		babyknuddel = Knuddel()
		print self.name, "und", knuddel.name, "haben jetzt ein Baby."
		return babyknuddel
	def benennen(self, name):
		if not hasattr(self, "name"):
			self.name = name
		else:
			raise KnuddelName("Dieses Knuddel hatte schon einen Namen.")
	
		
