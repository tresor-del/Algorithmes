from collections import deque


def bfs(graph, start, target=None):

    # initialisation d'un set pour les lieux déjà visités
    visited = set()
    
    # initialisation de la file avec un point de départ
    file = deque([start])  
    
    while file:
        # prend le premier elmt de la file
        debut = file.popleft()
        
        # si l'élément n'est pas visité, on l'ajoute(#1) et on ajoute tous ces voisins a la file(#2)
        if debut not in visited:
            print(debut)        
            
            visited.add(debut)   # 1
            
            if target and target == debut:
                print("Point trouvé !")
                break
            
            file.extend(sorted(graph[debut])) #2
            # file.extend(graph[debut])  #2, ou graphe.neighbors(debut) 
            
            print(f"Voisins de {debut}: ", graph[debut] )

def bfs_simple(g, start):
    V, E = g
    visite = set()
    file = deque([start])

    while file:
        
        debut = file.popleft()

        if debut not in visite:
            print(debut)

            visite.add(debut)

            for voisin in E[debut]:
                file.append(voisin)
            
            print("Voisin: ", E[debut])

# Exemple pour trouvé un point G
if __name__ == "__main__":
    
    from search.graphes.creation_graphe.main import G
    from search.graphes.creation_graphe.simple import g

    bfs(G, "A", "G")
    print("\n")
    bfs_simple(g, "a")

