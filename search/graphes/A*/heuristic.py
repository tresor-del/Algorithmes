import heapq  # module pour gérer une file de priorité (tas binaire)

def heuristic(a, b):
    # Fonction heuristique qui estime le coût restant entre deux nœuds
    # Ici, on utilise une distance "alphabétique" arbitraire
    # ord() donne le code ASCII d’un caractère, abs() la valeur absolue
    return abs(ord(a) - ord(b))

def astar(graph, start, goal):
    # Initialisation de la file de priorité avec le nœud de départ et un score f=0
    heap = [(0, start)]
    
    # Dictionnaire pour reconstruire le chemin final (clé = nœud, valeur = parent)
    came_from = {}
    
    # Dictionnaire des coûts g(n) initiaux (distance minimale connue depuis le départ)
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0  # Coût pour le départ = 0
    
    # Boucle principale tant qu’il y a des nœuds à explorer dans la file de priorité
    while heap:
        # On récupère le nœud avec la plus petite valeur f_score (f = g + h)
        _, current = heapq.heappop(heap)
        
        # Si on a atteint l’objectif, on reconstruit le chemin en remontant
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)  # On ajoute le point de départ au chemin
            return path[::-1]   # On renvoie le chemin dans le bon ordre
        
        # Pour chaque voisin du nœud courant
        for neighbor, cost in graph[current].items():
            # Calcul du coût total si on passe par current jusqu’au voisin
            tentative_g = g_score[current] + cost
            
            # Si ce chemin est meilleur que celui connu jusqu’ici
            if tentative_g < g_score[neighbor]:
                # On met à jour le parent du voisin
                came_from[neighbor] = current
                
                # On met à jour le meilleur coût g connu pour ce voisin
                g_score[neighbor] = tentative_g
                
                # Calcul du score f = g + heuristique estimée vers l’objectif
                f_score = tentative_g + heuristic(neighbor, goal)
                
                # On ajoute le voisin à la file de priorité avec son score f
                heapq.heappush(heap, (f_score, neighbor))
    
    # Si on sort de la boucle sans avoir trouvé l’objectif, pas de chemin possible
    return None
