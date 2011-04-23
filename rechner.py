def f(zeichenkette):
  if "(" in zeichenkette:
    k = zeichenkette.index(")")
    j = len(zeichenkette)-list(reversed(zeichenkette)).index("(", len(zeichenkette)-k)-1
    #print k, j
    zahl3 = f(zeichenkette[j+1:k])
    return f(zeichenkette[:j] + str(zahl3) + zeichenkette[k + 1:])
  if "+" in zeichenkette:
    i=zeichenkette.index("+")
    zahl1 = float(zeichenkette[:i])
    zahl2 = f(zeichenkette[i+1:])
    #print "Es befindet sich ein '+' in der Zeichenkette."
    zahl = zahl1 + zahl2 
  else:
    zahl=float(zeichenkette)
  return zahl

#eingabe = raw_input()
#print f(eingabe)
print f("2+2*(3+4+5)")


# ((2+3)+4)+5
