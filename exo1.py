from math import *
a = float(input("Saisir la valeur de l'entier a: "))
b = float(input("Saisir la valeur de l'entier b: "))

q = int(a / b)
r = int(a % b)
ratio = a/b
r1 = 0
if r == 0:
    print("Le quotient entier de la division est: ", q)
    print("Le reste de la division entière est: ", r)
else:
    print("Le quotient réel de la division est: ", ratio)
    print("Le reste de la division réelle est: ", r1)

