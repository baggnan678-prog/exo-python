# 1. Initialisation
TAILLE = int(input("Le tableau a combien de valeur :"))
tableau_entiers = []

# 2. Saisie Interactive (La Boucle For Limitée)
print("--- Initialisation interactive du tableau de 10 entiers naturels ---")
for i in range(TAILLE):
    # Boucle de validation (le côté osé : ne pas laisser l'utilisateur faire n'importe quoi !)
    while True:
        try:
            # Demande de saisie
            saisie = input(f"Entrez l'entier naturel {i + 1}/{TAILLE} : ")
            
            # Conversion en entier
            valeur = int(saisie)
            
            # Validation : doit être un entier naturel (>= 0)
            if valeur < 0:
                print("🚨 Erreur : L'entier doit être naturel (positif ou nul). Réessaie.")
            else:
                # Saisie valide, on ajoute et on sort de la boucle while
                tableau_entiers.append(valeur)
                break
        
        except ValueError:
            # Gère le cas où l'utilisateur entre du texte au lieu d'un nombre
            print("🛑 Erreur de format : Ce n'est pas un entier. Réessaie.")

# 3. Affichage du Résultat
print("\n--- Le tableau est complet ! ---")
print(f"Ton tableau final de {TAILLE} éléments est : {tableau_entiers}")
