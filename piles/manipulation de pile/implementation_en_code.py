def deplacer_piles(P1):
    """
    Déplace les éléments de P1 dans P2 de sorte que :
      - pairs en haut (ordre conservé)
      - impairs en bas (ordre inversé)
    En utilisant une pile intermédiaire P3.
    Retourne P2 et restaure P1.
    """
    P2 = []   # résultat final
    P3 = []   # pour stocker les pairs
    sauvegarde = []  # pour restaurer P1 à la fin

    # Étape 1 : vider P1
    while P1:  
        x = P1.pop()
        sauvegarde.append(x)
        if x % 2 == 0:     # pair
            P3.append(x)
        else:              # impair
            P2.append(x)

    # Étape 2 : restaurer P1
    while sauvegarde:
        P1.append(sauvegarde.pop())

    # Étape 3 : transférer pairs de P3 vers P2
    while P3:
        P2.append(P3.pop())

    return P2


###Exemple concret 
# P1 = pile initiale (bas = premier élément, haut = dernier élément)
P1 = [5, 8, 7, 2, 9]  

P2 = deplacer_piles(P1)

print("Pile P1 après exécution :", P1)   # doit être restaurée
print("Pile P2 obtenue :", P2)
