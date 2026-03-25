import random
taille = 100
tableau = []
d = int(input("De quel chiffre voulez vous connaitre l'indice : "))

for i in range(taille):
    a = random.randint(0,1000)
    tableau.append(a)
    if a==d :
      p=i
      print(f"l'indice du premier {d} est de {p}")
   
tableau2 = [z for z in tableau if z < 10]
# .sort sert à ordonné le tableau et tt ce qui est l'intérieur des crochet du tableau2 est une condition d'ajout au tableau , z est une variable utiliser pour fixer cette condition
tableau2.sort()
# . count permet de savoir combien de fois un nombre apparait dans une liste et s'utilise exactement comme la fonction .index
n = tableau.count(d)

b = min(tableau)
c= max(tableau)
print(tableau)
print (f"la plus petite valeur est {b}")
print(f"la plus grande valeur est {c}")
print(f"Le nombre de {d} est de {n}")
print(f"Les valeurs inférieur à 10 sont {tableau2[::-1]} et la somme est {sum(tableau2)}")
tableau3= [q for q in tableau if q%2==0]
print(f"Les nombre paire du tableau sont {tableau3} et  leurs somme est {sum(tableau3)}")
