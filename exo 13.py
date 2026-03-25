taille = 1000
tableau = []
for i in range(taille):
    import random
    a = random.randint(1,1000)
    tableau.append(a)
b = min(tableau)
c= max(tableau)
print(tableau)
print (f"la plus petite valeur est {b}")
print(f"la plus grande valeur est {c}")