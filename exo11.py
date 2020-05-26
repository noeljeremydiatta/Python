from math import *

a = int(input("entrer la valeur de l’entier a: "))
b = int(input("entrer la valeur de l’entier b: "))
signe = str(input("Veuillez choisir un opérateur parmi les suivants + ou - ou * ou /: "))

if signe == "+":
    result = a + b
    print("Le résultat de l’opération est :", result)
elif signe == "-":
    result = a - b
    print("Le résultat de l’opération est :", result)
elif signe == "*":
    result = a * b
    print("Le résultat de l’opération est :", result)
else:
    result = int(a / b)
    print("Le résultat de l’opération est :", result)
