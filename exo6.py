from math import *

x1 = float(input("Saisir la valeur de x1: "))
y1 = float(input("Saisir la valeur de y1: "))
x2 = float(input("Saisir la valeur de x2: "))
y2 = float(input("Saisir la valeur de y2: "))

dist = round(sqrt((x1 - x2)**2 + (y1 - y2)**2))

print("la distance entre les points A et B est: ", dist)
