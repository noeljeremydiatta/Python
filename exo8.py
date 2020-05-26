from math import *

a = float(input("Saisir la valeur de a: "))
b = float(input("Saisir la valeur de b: "))
c = float(input("Saisir la valeur de c: "))

delta = int(b ** - 4 * a * c)

if delta < 0:
    print("l'équation n'apas de solution")
elif delta == 0:
    x0 = int(- b / 2 * a)
    print("la solution de l'équation est: ", x0)
else:
    x1 = int((-b - sqrt(delta)) / 2 * a)
    x2 = int((-b + sqrt(delta)) / 2 * a)
    print("la solution de l'équation est: {", x1, ";", x2, "}")
