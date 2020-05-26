from math import *

a = float(input("Saisir la valeur de l'entier a: "))
b = float(input("Saisir la valeur de l'entier b: "))


reste = int(a % b)
PGCD = int(a - reste)
PPCM = int(a * b / PGCD)

print("le plus grand commun diviseur est:", PGCD)
print("le plus petit commun diviseur est:", PPCM)
