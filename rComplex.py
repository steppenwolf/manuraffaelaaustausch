#! /usr/bin/python
# -*- coding: utf-8 -*-

import math

class Complex(object):
	def __init__(self, a, b=0):
		if isinstance(a,str):
			self.real = float(a[:a.find(',')])
			self.imag = float(a[a.find(',')+1:])
		else:
			self.real = a
			self.imag = b
	def get_abs(self):
		return math.sqrt(self.real * self.real + self.imag * self.imag)
	def set_abs(self, abs_):
		streckfaktor = float(abs_)/self.get_abs()
		self.real = self.real * streckfaktor
		self.imag = self.imag * streckfaktor
	abs = property(get_abs, set_abs)
	def __str__(self):
		return str(self.real) + ',' + str(self.imag)
	def __add__(self, summand):
		return Complex(self.real + summand.real, self.imag + summand.imag)
	def __mul__(self, faktor):
		if isinstance(faktor, Complex):
			return Complex(self.real*faktor.real-self.imag*faktor.imag, self.real*faktor.imag+self.imag*faktor.real)
		else:
			return Complex(self.real*faktor, self.imag*faktor)
