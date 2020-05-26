from math import *

montant = int(input("Veuillez saisir le montant à décomposer: "))

if montant > 20:
    {}
bi20 = int(montant / 20)
reste = montant % 20
print(bi20, "billets de 20 euros")

if montant > 10:
    {}
bi10 = int(reste / 10)
reste = reste % 10
print(bi10, "billets de 10 euros")

if montant > 5:
    {}
bi5 = int(reste / 5)
reste = reste % 5
print(bi5, "billets de 5 euros")

if montant > 2:
    {}
pi2 = int(reste / 2)
reste = reste % 2
print(pi2, "pièces de 2 euros")

if montant > 1:
    {}
pi1 = int(reste / 1)
reste = reste % 1
print(pi1, "pièces de 1 euros")
