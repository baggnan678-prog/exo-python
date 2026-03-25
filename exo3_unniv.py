article = input('Quel est le produit que vous voulez : ')
quantité = int(input(f"Quel est la quantité de {article} que vous voulez : "))
prix = int(input("Honnêtement quel est le prix unitaire de l'article : "))
facture = quantité*prix
if facture>1000 : 
    reduc=(facture*1)/100
    factur=facture-reduc
    print(f"Félicitation vous bénéficier d'une remise de 1% , votre facture est donc de {factur} au lieu de {facture}")
else:
    print(f"Malheureusement vous passer à coté d'une belle réduction , si votre facture était supérieur à 1.000f vous l'aurier eu . Vous nous devez donc {facture}")