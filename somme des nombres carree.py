

def somme_nombres_pairs_python():
    """Calcule la somme des nombres pairs à partir de 0 jusqu'à une limite N définie par l'utilisateur."""
   
    # Demander à l'utilisateur de saisir la limite
    try:
        limite = int(input("Jusqu'à quel nombre (inclusif) dois-je calculer la somme des pairs (à partir de 0) ? "))
    except ValueError:
        print("Saisie invalide. Veuillez entrer un nombre entier.")
        return

    # Vérifier si la limite est négative
    if limite < 0:
        print("Veuillez entrer un nombre positif ou nul.")
        return

    # Utiliser une compréhension de liste avec la fonction range()
    # range(start, stop, step) : commence à 0, s'arrête avant limite+1, avance de 2 en 2
    # Si la limite est par exemple 10, range(0, 11, 2) génère 0, 2, 4, 6, 8, 10
   
    somme = sum(range(0, limite + 1, 2))
   
    print(f"\nLa somme des nombres pairs de 0 à {limite} est : {somme}")

if __name__ == "__main__":
    somme_nombres_pairs_python()