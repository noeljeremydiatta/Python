secret = 7
nombre = int(input("Saisir un nombre: "))
while nombre < secret:
    print("plus petit")
    nombre = int(input("Saisir un nombre: "))

    while nombre > secret:
        print("plus grand")
        nombre = int(input("Saisir un nombre: "))

if nombre == secret:
    print("Bravo vous avez deviné le nombre secret qui est: ", secret)
