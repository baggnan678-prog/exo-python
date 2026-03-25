print("EXERCICE 1(total des valeurs jusqu'à un nombre )")
print("")
a=float(input("Saisisser un nombre : "))
b=1
c=a*(a+1)
c=c/2
print("La somme des valeurs jusqu'à ce nombre est : ",c)
print("")

print("EXERCICE 2(Max et Min d'une liste donné )")
print("")

a=0
print("NB:Si vous arrivé a la dernière valeur de votre liste écrivé 'fin' au niveau de la lettre c ")
print("Si votre liste n'est pas fini appuyez sur 'entré'")
print("")
li=[]
while a > -1  :
 b=int(input("Entré un élément de votre liste :"))
 li.append(b)
 c=str(input("c :"))
 if c=="fin" :
  break

li.sort()
print("Le plus petit element de votre liste est :") ;print(li[0])
print("Le plus grand element de votre liste est :") ;print(li[-1])

print("")
print("EXERCICE 3 (trouver le quotien et le reste d'une division )")
print("")

a=int(input("Quel est le diviseur : "))
b=int(input("Quel est le dividande : "))
c=b%a
print("Le reste de la division est", c)
d=(c+b)/a
print("Le quotient de la division est", d)
print("")

print("EXERCICE 4")
print("")




























print("")
print("EXERCICE 5 (divisibilité d'un nombre par un autre)")
print("")

a=int(input("Entré un nombre : "))
b=int(input("Par quel nombre voulez vous savoir si le nombre précédent est divisible : " ))
if a%b==0 :
  print("Oui, ces nombres sont divisibles")
else :
 print("Non , ils ne sont pas divisibles")

print("")
print("EXERCICE 6")
print("")


