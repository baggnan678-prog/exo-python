taille = 10
tableau = []
for i in range(taille):
    import random
    import math
    a = random.randint(-10,10)
    tableau.append(a)
n = tableau[0:10]
p = math.prod(n)
print(f"Voice votre tableau {tableau}")
print(f"Le produit des valeurs du tableau est de {p}")