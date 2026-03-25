a=0
print("NB:Si vous arrivé a la dernière valeur de votre liste écrivé 'oui' n'importe quel autre valeur ne comptera pas et la liste continuera ")
print("Si votre liste n'est pas fini appuyez sur 'entré'")
print("")
li=[]
while a > -1  :
 b=float(input("Entré un élément de votre liste :"))
 li.append(b)
 c=str(input("votre liste est fini :"))
 if c=="oui" or c=="Oui" :
  break

li.sort()
print("Le plus petit element de votre liste est :",li[0])
print("Le plus grand element de votre liste est :",li[-1])

