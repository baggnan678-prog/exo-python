a=float(input("Veuiller entre une valeur ( il existe 3 bonne réponse) :"))
if a<=3 and a>=1 :
    print("Bravooo")
while a>3 or a<1:
    a=float(input("Mauvaise reponse , ressayer : "))
    if a <= 3 and a >= 1:
        print("Bravooo")
    break