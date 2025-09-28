

def d_simple(G, start):
    
    # mettre les distances a l'infini
    distances = {noeud: float("inf") for noeud in G}
    
    # mettre la distance du noeud de début à 0
    distances[start] = 0
    
    visite = set()

    while len(visite) < len(G):

        noeud_actuel = min(
            (noeud for noeud in G if noeud not in visite),
            key=lambda noeud: distances[noeud]
        )
        visite.add(noeud_actuel)

        for voisin, poids in G[noeud_actuel].items():
            distance = distances[noeud_actuel] + poids
            if distance < distances[voisin]:
                distances[voisin] = distance
    
    return distances


if __name__ == "__main__":
    
    G = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "C": 1, "D": 4},
        "C": {"A": 5, "B": 1, "D": 2},
        "D": {"B": 4, "C": 2}
    }
    
    print(d_simple(G, "A"))
