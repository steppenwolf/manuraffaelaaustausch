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
  def abs(self):
    return math.sqrt(self.real * self.real + self.imag * self.imag)
  def __str__(self):
    return str(self.real) + ',' + str(self.imag)
  def __add__(self, summand):
    return Complex(self.real + summand.real, self.imag + summand.imag)
  def __mul__(self, summand):
    return Complex(self.real*summand.real-self.imag*summand.imag, self.real*summand.imag+self.imag*summand.real)
