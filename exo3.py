
r1 = float(input("Saisir la valeur de la résistance: "))
r2 = float(input("Saisir la valeur de la résistance: "))
r3 = float(input("Saisir la valeur de la résistance: "))
choice = int(input("Précisez votre choix en tapant 1 ou 2: "))

rs = (r1 + r2 + r3)
rp = ((r1 * r2 * r3) / (r1 * r2 + r2 * r3 + r3 * r1))

if choice == 1:
    print("la fréquence en série est: ", rs)
else:
    print("la fréquence en paralléle est: ", rp)
