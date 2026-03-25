taille = 1000
tableau = []
n = 0
for i in range(taille):
    import random
    a = random.randint(0,1000)
    if a==0 :
      n = n+1
    tableau.append(a)
d = tableau.index(0)
b = min(tableau)
c= max(tableau)
print(tableau)
print (f"la plus petite valeur est {b}")
print(f"la plus grande valeur est {c}")
print(f"Le nombre d'élément nul est de {n}")
print(f"l'indice du premier 0 est de {d}")