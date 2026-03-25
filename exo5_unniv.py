saisi = float(input("Saississez la valeur de a :"))
while saisi== 0 : 
    saisi = float(input("Saississez la valeur de a :"))
saisi2 = float(input("Saississez la valeur de b :"))
saisi3 = float(input("Saississez la valeur de c :"))
delt  = 0
saisi2 = saisi2*saisi2
delt = (4*(saisi*saisi3))
delt = saisi2 - delt

if delt > 0 : 
    x1 = -saisi2 - (delt**0,5)
    x1 = x1/(2*saisi)
    x2 = -saisi2 + (delt**0,5)
    x2 = x2/(2*saisi)
    print(f"La solution x1 est {x1} la solution x2 {x2}")
elif delt == 0 :
    saisi2 = saisi2/saisi2
    x1 = -saisi2/(2*saisi)
    print (f"La solution est {x1}")
else : 
    print (" Il n'existe pas de solution")
