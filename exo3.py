i=0
li=str("Seydou")
while i < 7 :
 a=str(input("Choisissez une lettre :" ))
 if a in li:
  print("Bravoooo le mot est Seydou")
  break
 else:
  i = i + 1
  print("il vous reste", 7-i ,str("vies"))