nombre = int(input("Entrée un nombre compris entre 1 et 10 :"))
while nombre<1 or nombre>10 : 
    nombre=int(input("Veuillez entrer une valeur valide (entre 1 et 10 :)"))
o=0
for i  in range (11):
    print(f"{nombre} multiplier par {o} = {nombre*o}")
    o=o+1
