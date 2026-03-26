#code pour savoir entre 2 frere qui sera majeur ou mineur 


#récupération des informations
amine=int(input("Quel âge a Amine :"))
ryan=int(input("Quel âge a Ryan :"))

#l'âge de amine dans 5 ans et ryan dans 10 ans 
print("Dans 5 ans Amine aura",amine+5,"ans")
print("Dans 10 ans Ryan aura",ryan+10,"ans")

#obtention des année de départ amine
annee=int(input("en quel année Amine avait cette âge : "))
fut=int(input("vous souhaiter connaitre l'âge de Amine en quel annee :"))

#calcul
dif=fut-annee
amine=amine+dif

#affichage résultat pour amine
print("Amine aura",amine,"ans en",fut)

#obtention des année de depart ryan
annee=int(input("en quel annéé Ryan avait cette âge : "))
fut=int(input("vous souhaiter connaitre l'âge de Ryan en quel annee :"))

#calcul
dif=fut-annee
ryan=ryan+dif

#condition et résultat pour savoir s'il seront mineur ou majeur 
print("Ryan aura",ryan,"ans en",fut)
if ryan>=18 and amine>=18 :
    print("Ils seront tout les 2 majeurs ")
elif ryan>=18 and amine<18:
    print("Ryan sera majeur en 2025 et Amine non")
elif amine>=18 and ryan<18  :
    print("amine sera majeur en 2025 et Ryan non")
elif ryan<18 and amine<18:
    print("Ils seront tous les 2 mineurs en 2025")