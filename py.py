import random
taille = 1000
tableau = []
n = 0
d = int(input("De quel chiffre voulez vous connaitre l'indice : "))

for i in range(taille):
    a = random.randint(0,1000)
    tableau.append(a)
    if a==d :
      n = n+1
      p=i
      print(f"l'indice du premier {d} est de {p}")
   


b = min(tableau)
c= max(tableau)
print(tableau)
print (f"la plus petite valeur est {b}")
print(f"la plus grande valeur est {c}")
print(f"Le nombre de {d} est de {n}")
