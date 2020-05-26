from math import *

hd = float(input("Donner l'heure de départ du vol: "))
md = float(input("Donner les minutes de départ du vol: "))
ha = float(input("Donner l'heure d'arrivée du vol: "))
ma = float(input("Donner les minutes d'arrivée du vol: "))

d = 60 * hd + md
a = 60 * ha + ma
dur = float(a) - float(d)

if dur > 60:
    {}
h = int(dur / 60)
m = int(dur % 60)

if a < d:
    hd = float(input("Donner l'heure de départ du vol"))
    md = float(input("Donner les minutes de départ du vol"))
    ha = float(input("Donner l'heure d'arrivée du vol"))
    ma = float(input("Donner les minutes d'arrivée du vol"))

print("la durée du vol est de ", h, "heure(s) et de ", m, "minute(s)")
