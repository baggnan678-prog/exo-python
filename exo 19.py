matrice1 = []
matrice2 = []
matrice3 = []
taille = 3
for i in range(taille):
    a=input("Choisisser les valeurs de la 1ère ligne :")
    matrice1.append(a)
for i in range(taille) :
    b=input("Choisisser les valeurs de la 2ème ligne :")
    matrice2.append(b)
matrice3.append(matrice1)
matrice3.append(matrice2)
print(f"La matrice final est {matrice3}")