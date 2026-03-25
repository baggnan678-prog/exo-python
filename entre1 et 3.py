b=0
a=float(input("Veuiller entre une valeur ( il existe 3 bonne réponse et vous avez 9 vies) : "))
i=1
while b>-1:
    if a>3 or a<1:
     a=float(input("Mauvaise reponse , ressayer : "))
    if a <= 3 and a >= 1:
        print("Bravooo")
        break
    i=i+1
    if i==3 :
       d=str(input("voulez vous un indice : "))
       if d=="oui" or d=="Oui":
          print("Le nombre est inférieur à 10")
    if i==6 :
       d=str(input("voulez vous un autre indice : "))
       if d=="oui" or d=="Oui":
          print("Le nombre est impaire")
    if i==9:
       print("Vous avez perdu ")
       break