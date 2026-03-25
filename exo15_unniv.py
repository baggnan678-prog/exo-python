Note=float(input("Quel à été ta Note : "))

if 14 > Note >= 12:
 print("Assez bien")
elif 16 > Note >= 14:
  print("Bien")
elif 18 > Note >= 16:
  print("Tres bien")
elif 20>= Note >= 18:
  print("Les felicitation du jury")
elif 0<=Note<10 :
    print(" Attention tu risque la session")
elif 10<=Note<12 :
    print("Faible, tu peut faire mieux")
else:
  print("Pas de Note")
