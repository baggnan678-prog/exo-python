entree=input("Etes vous assurer chez nous depuis plus de 1 ans :")
if entree=="oui" or entree=="Oui" :
    print("Merci de votre fidélité , comme preuve de remerciement nous vous offront le tarif bleu ")
    breakpoint()
else:
    print("Bienvenus chez naughty boy assurance , l'assurance de plus de 90% des vilain garçons , j'espere que vous apprévierer nos service ")
age=int(input("Quel âge a le postulant de l'assurace : "))
permi=int(input("Depuis combien de temp a t'il sont permis : " ))
print("Veuiller répondre juste en minuscule")
responsabilite=input("A t'il déja cosé un accident :")
if age<25 and permi<2 and responsabilite=="oui" :
    print("Nous sommes vraiment désolé mais nous ne pouvons pas vous assurer ")
if (age<25 and permi<2 and responsabilite=="non") :
    print("Nous vous proposons le tarif rouge")
if age<25 and permi>=2 and responsabilite=="non" :
    print("Nous vous proposons le tarif orange")
if age<25 and permi>=2 and responsabilite=="oui":
    nb_accident=int(input("De combien d'accident etes vous responsable : "))
    if nb_accident>1 :
        print("Nous sommes vraiment désolé mais nous ne pouvons pas vous assurer")
    else:
        print("Nous vous proposons le tarif rouge")
if age>=25 and permi>=2 and responsabilite=="non" :
    print("Nous vous proposons le tarif vert ")
if age>=25 and permi>=2 and responsabilite=="oui" :
    nb_accident=int(input("De combien d'accident etes vous responsable : "))
    if nb_accident>2 :
        print("Nous sommes vraiment désolé mais nous ne pouvons pas vous assurer")
    elif nb_accident==2:
        print("Nous vous proposons le tarif rouge")
    elif nb_accident == 1:
        print("Nous vous proposons le tarif orange")
if age>=25 and permi<2 and responsabilite=="non" :
    print("Nous vous proposons le tarif orange")
if age>=25 and permi<2 and responsabilite=="oui" :
    nb_accident=int(input("De combien d'accident etes vous responsable : "))
    if nb_accident > 1:
        print("Nous sommes vraiment désolé mais nous ne pouvons pas vous assurer")
    else:
        print("Nous vous proposons le tarif rouge")