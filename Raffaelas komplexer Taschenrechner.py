#! /usr/bin/python
# -*- coding: utf-8 -*-

import rComplex


def summe(x, y):
  return x+y

def produkt(x, y):
  return x*y


rechenarten = { 'a': ('addieren', 'Die Summe', 0, summe), 'm': ('multiplizieren', 'Das Produkt', 1, produkt) }

modus = ''
while not modus in rechenarten.keys():
  print 'Wollen sie addieren (a) oder multiplizieren (m)?'
  modus = raw_input()


rechenart_verb, rechenart_ergebnis, neutrales_element, rechenart = rechenarten[modus]

versuche = 0

anzahl = 2
while versuche < 5:
  try:
    print 'Wie viele Zahlen wollen Sie ' + rechenart_verb + '?'
    anzahl = int(raw_input())
    if anzahl <= 0:
      raise ValueError
    break
  except ValueError:
    versuche = versuche + 1
    print 'Sie haben keine natürliche Zahl eingegeben. Dies war Versuch Nummer', versuche, 'von 5.'

zahlen = []

for index in range(anzahl):
  try:
    print 'Bitte geben Sie Zahl', index, 'ein.'
    zahlen.append(rComplex.Complex(raw_input()))
  except ValueError:
    print 'Sie haben keine korrekte Zahl eingegeben! Zahl', index, 'wird ignoriert.'

zwischenergebnis = rComplex.Complex(neutrales_element)
for zahl in zahlen:
  zwischenergebnis = rechenart(zwischenergebnis, zahl)
  
print rechenart_ergebnis, 'der Zahlen', '; '.join([str(zahl) for zahl in zahlen]), 'ist', zwischenergebnis, '.'
# hallo manu <3