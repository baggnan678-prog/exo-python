taille = 20
tableau = []
o=1
for i in range(taille):
    a = float(input(f"Entrez le nombre numéro {o} : "))
    tableau.append(a)
    o=o+1
b = min(tableau)
d = tableau.index(b)
c= max(tableau)
p=tableau.index(c)
print(tableau)
print (f"la plus petite valeur est {b} , c'était le nombre {d+1}")
print(f"la plus grande valeur est {c} , c'était le nombre {p+1}")