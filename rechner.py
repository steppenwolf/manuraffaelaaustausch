#! /usr/bin/python
# -*- coding: utf-8 -*-

def strtolist(zeichenkette):
	liste = []
	zwischenspeicher = ""
	for zeichen in zeichenkette:
		if zeichen in "()+-*/":
			if zwischenspeicher:
				liste.append(float(zwischenspeicher))
				zwischenspeicher = ""
			liste.append(zeichen)
		else:
			zwischenspeicher += zeichen
	if zwischenspeicher:
		liste.append(float(zwischenspeicher))
	return liste


def f(liste):
	print liste
	if "(" in liste:
		k = liste.index(")")
		j = len(liste)-list(reversed(liste)).index("(", len(liste)-k)-1
		#print k, j
		zahl3 = f(liste[j+1:k])
		return f(liste[:j] + [zahl3] + liste[k + 1:])
	if "+" in liste:
		i=liste.index("+")
		zahl1 = f(liste[:i])
		zahl2 = f(liste[i+1:])
		#print "Es befindet sich ein '+' in der liste."
		zahl = zahl1 + zahl2 
	elif "-" in liste:
		i= len(liste) - list(reversed(liste)).index("-") -1
		if i == 0:
			zahl1 = 0
		else:
			zahl1 = f(liste[:i])
		zahl2 = f(liste[i+1:])
		#print "Es befindet sich ein '-' in der liste."
		zahl = zahl1 - zahl2 
	elif "*" in liste:
		i=liste.index("*")
		zahl1 = f(liste[:i])
		zahl2 = f(liste[i+1:])
		zahl = zahl1 * zahl2
	elif "/" in liste:
		i= len(liste) - list(reversed(liste)).index("/") -1
		zahl1 = f(liste[:i])
		zahl2 = f(liste[i+1:])
		#print "Es befindet sich ein '/' in der liste."
		zahl = zahl1 / zahl2 
	else:
		zahl = liste[0]
	return zahl

#~ eingabe = raw_input()
#~ print f(eingabe)


print f(strtolist("-1"))

#TODO:
#1/(2-5)*6/3
# => [1, "/", "(", 2, "-", 545, ")", "*", 6, "/" 3]

# Code aufräumen

# Objektorientierung
