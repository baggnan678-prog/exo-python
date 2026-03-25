pSeuil=2.3
vSeuil=7.41
pcourrant=float(input("Entrez la préssions courante : "))
vcourrant=float(input("Entrez le volume courant : "))
if pcourrant>pSeuil and vcourrant>vSeuil : 
    print("ARRET IMMEDIAT")
elif pcourrant>pSeuil:
    print("Augmentez le volume de l'enceinte")
elif vcourrant>vSeuil:
    print("Diminuer le volume de l'enceinte ")
else:
    print("Tout vas bien")