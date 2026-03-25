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
#li.sort permet d'ordonné la liste
li.sort()
print("Le plus petit element de votre liste est :") ;print(li[0])
print("Le plus grand element de votre liste est :") ;print(li[-1])
