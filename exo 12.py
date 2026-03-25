taille = 100
tableau = []
for i in range(taille):
    import random
    a = random.randint(1,100)
    tableau.append(a)
b = min(tableau)
print(tableau)

print (f"la plus petite valeur {b}")
