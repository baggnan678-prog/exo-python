taille = 1000
tableau = []
tab = []
n = 0
z = int(input("Quel est la valeur dont vous vous voulez connaitre la fréquence d'apparition : "))
for i in range(taille):
    import random
    a = random.randint(-1000,1000)
    if a==z :
      n = n+1
    tableau.append(a)
b = min(tableau)
c= max(tableau)
print(tableau)
print (f"la plus petite valeur est {b}")
print(f"la plus grande valeur est {c}")
print(f"Le nombre de répétition de {z} est de {n}")