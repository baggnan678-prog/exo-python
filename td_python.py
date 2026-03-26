import random
entree=int(input("entrer le nombre d'element que doit contenir le  tableau : "))
tableau = [random.randint(1,1000) for _ in range(entree)]
tableau2 = [paire for paire in tableau if paire%2==0]
print(f"Voici le premier tableau {tableau}")
tableau3=tableau2.sort()
print(f"les nombres paire du tableau sont {tableau2} et dans l'ordre sa fera {tableau3}")