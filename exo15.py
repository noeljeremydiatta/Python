nombre = int(input("saisir un chiffre: "))

somme = 0
for i in range(1, nombre + 1, 1):
    somme = somme + i
    moyenne = somme / nombre

print("Le nombre de départ est: ", nombre)
print("La somme des entiers jusqu'à", nombre, "est: ", somme)
print("La moyenne est: ", moyenne)
