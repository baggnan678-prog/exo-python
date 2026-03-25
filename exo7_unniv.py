montant = float(input("Veuillez entré le montant de votre salaire : "))
statut = int(input("Veuillez entrer votre situation matriomoniale (0 pour dire célibataire de 1 pour dire Marié): "))
while statut != 0 and statut != 1 : 
      statut = int(input("Veuillez entrer votre situation matriomoniale (0 pour dire célibataire de 1 pour dire Marié): "))
if montant<2000000 :
    if statut==0 :
        net = montant * (1)
        print(f"Le salaire net est de {net}")
        break
    elif statut == 1 :
        net = montant * (1)
        print(f"Le salaire net est de {net}")
elif 2000000<=montant<=10000000 : 
    if statut==0 :
        net = montant * (1-0.1)
        print(f"Le salaire net est de {net}")
    if statut==1 :
        net = montant * (0.95)
        print(f"Le salaire net est de {net}")
else : 
    if statut==0 :
        net = montant * (1-0.2)
        print(f"Le salaire net est de {net}")
    if statut==1 :
        net = montant * (0.85)
        net1 = float(net)
        print(f"Le salaire net est de {net1}")