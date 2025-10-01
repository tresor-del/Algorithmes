def tours_de_hanoi(n, source, destination, auxiliaire):
    """
    Résout le problème des Tours de Hanoï.

    Args:
        n (int): Le nombre de disques à déplacer.
        source (str): Le nom de la pile de départ (e.g., 'A').
        destination (str): Le nom de la pile d'arrivée désirée (e.g., 'B').
        auxiliaire (str): Le nom de la pile temporaire (e.g., 'C').
    """
    # 1. Cas de Base : Condition d'arrêt de la récursion
    if n == 1:
        print(f"Déplacer le disque 1 de la pile {source} vers la pile {destination}")
        return

    # 2. Étape Récursive

    # A. Déplacer les n-1 disques supérieurs de Source vers Auxiliaire
    #    (La Destination devient la pile temporaire)
    tours_de_hanoi(n - 1, source, auxiliaire, destination)

    # B. Déplacer le n-ième disque (le plus grand) de Source vers Destination
    print(f"Déplacer le disque {n} de la pile {source} vers la pile {destination}")

    # C. Déplacer les n-1 disques d'Auxiliaire vers Destination
    #    (La Source devient la pile temporaire)
    tours_de_hanoi(n - 1, auxiliaire, destination, source)

# Exemple avec 3 disques
nombre_de_disques = 3
print(f"--- Résolution pour N = {nombre_de_disques} disques (A -> C) ---")
tours_de_hanoi(nombre_de_disques, 'A', 'C', 'B')