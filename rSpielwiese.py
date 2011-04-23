#! /usr/bin/python
# -*- coding: utf-8 -*-

#~ import rComplex
#~ 
#~ zahl1 = rComplex.Complex('3,2')
#~ zahl2 = rComplex.Complex(1)

#print 'Der Betrag ist', zahl2.abs(), '.'

#print 'Der Realteil ist', zahl2.real, '.'
#print 'Der Imaginärteil ist', zahl2.imag, '.'

#~ print zahl1 + zahl2
#~ print zahl1*zahl2

#zahl von knuddel

import knuddel

bla = knuddel.Knuddel("Raffaela")

blub = knuddel.Knuddel("Manuel")

bla.begruessen(blub)
bla.knuddeln(blub)

baby = bla + blub

baby.benennen("Lilly") 
baby.vorstellung()
