#code pour connaitre l'age d'une personne en 2050

#déclaration des variables
age=int(input("Quel âge a la personne :"))
annee=int(input("en quel annéé la personne avait cette âge : "))

#calcule
dif=2050-annee
age=age+dif

#résultat finale
print(f"La personne aura {age} en 2050")