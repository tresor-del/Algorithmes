from collections import deque


def bfs(graph, start, target):

    # initialisation d'un set pour les lieux déjà visités
    visited = set()
    
    # initialisation de la file avec un point de départ
    queue = deque([start])  
    
    while queue:
        # prend le premier elmt de la file
        vertex = queue.popleft()
        
        # si l'élément n'est pas visité, on l'ajoute(#1) et on ajoute tous ces voisins a la file(#2)
        if vertex not in visited:
            print(vertex)        
            visited.add(vertex)   # 1
            
            print("Visite: ", visited)
            
            if target == vertex:
                break
            
            queue.extend(sorted(graph[vertex]))
            # queue.extend(graph[vertex])  #2, ou graphe.neighbors(vertex) 
            
            print(f"Voisins de {vertex}: ",queue)

if __name__ == "__main__":
    
    from creation_graphe.main import G

    bfs(G, "A", "G")

