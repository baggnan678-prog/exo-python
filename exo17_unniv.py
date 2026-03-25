import random
mys=random.randint(1,100)
#print(mys)
nombre  = int(input("Tentez votre chance de trouvez le nombre mystère :"))
o=1
while nombre!=mys : 
    if nombre<mys:
        nombre=int(input("Mauvaise réponse , le nombre est plus grand , réessayer :"))
    else :
         nombre=int(input("Mauvaise réponse , le nombre est plus petit , réessayer :"))
    o=o+1
print(f"Félicitation il vous aura fallut {o} essaies")