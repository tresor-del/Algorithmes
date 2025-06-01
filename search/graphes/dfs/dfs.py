import heapq  # module pour la file de priorité (tas binaire)

def dijkstra(graph, start):
    # Initialisation des distances : infini pour tous les noeuds sauf le départ
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # distance du départ à lui-même = 0

    # Tas (file de priorité) contenant les noeuds à explorer, triés par distance
    heap = [(0, start)]  # (distance, noeud)

    # Tant que la file de priorité n'est pas vide
    while heap:
        # On récupère le noeud avec la plus petite distance actuelle
        current_dist, current_node = heapq.heappop(heap)

        # Si la distance récupérée est plus grande que celle déjà connue, on ignore ce noeud
        if current_dist > distances[current_node]:
            continue

        # Pour chaque voisin du noeud courant
        for neighbor, weight in graph[current_node].items():
            # Calcul de la distance totale en passant par le noeud courant
            distance = current_dist + weight

            # Si cette distance est meilleure que celle déjà enregistrée
            if distance < distances[neighbor]:
                # Mise à jour de la distance la plus courte trouvée jusqu'ici
                distances[neighbor] = distance
                # Ajout du voisin dans la file de priorité avec sa nouvelle distance
                heapq.heappush(heap, (distance, neighbor))

    # Retourne le dictionnaire des distances minimales du départ vers tous les noeuds
    return distances
