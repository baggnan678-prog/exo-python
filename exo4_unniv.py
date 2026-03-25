article = input('Quel est le produit que vous voulez : ')
quantité = int(input(f"Quel est la quantité de {article} que vous voulez : "))
prix = int(input("Honnêtement quel est le prix unitaire de l'article hors taxe : "))
tva = float(input("Quel est le montant de la TVA dans votre pays : "))
ttc = prix*(1+(tva/100))
facture=quantité*ttc
if quantité<=5 :
    remise=facture*0.05
    factur  = facture-remise
    print(f"Félicitation vous avez une remise de 0,5% pour votre achat de {article} vous devez donc payer {factur} au lieu de {facture} ")
elif 5<quantité<=10 :
    remise=facture*0.075
    factur  = facture-remise
    print(f"Félicitation vous avez une remise de 0,75% pour votre achat de {article} vous devez donc payer {factur} au lieu de {facture} ")
if quantité>10 :
    remise=facture*0.1
    factur  = facture-remise
    print(f"Félicitation vous avez une remise de 10% pour votre achat de {article} vous devez donc payer {factur} au lieu de {facture} ")

