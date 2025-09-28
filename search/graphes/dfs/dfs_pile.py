from collections import deque

def dfs(graphe, start):
    visite = set()
    pile = deque([start])
    ordre_parcours = []
    
    while pile:
        # prendre le dernier element (a la différence de popleft() pour la file)
        sommet = pile.pop()
        
        if sommet not in visite:
            
            print(f"Noeud {sommet}")
            
            visite.add(sommet)
            ordre_parcours.append(sommet)    
            
            for voisin in graphe[sommet]:
                if voisin not in visite:
                    pile.append(voisin)
            
            print(f"Voisins de {sommet}: {graphe[sommet]}")
            
    {"ordre de parcours":ordre_parcours,"Noeuds visités":visite}

def dfs_simple(G, start):
    V, E = G
    visite = set()
    pile = [start]
    ordre_parcours = []

    while len(pile) > 0:
        sommet = pile.pop()
        
        if sommet not in visite:
            
            print(f"Noeud {sommet}")
             
            visite.add(sommet)
            ordre_parcours.append(sommet)
            
            for voisin in E[sommet]:
                if voisin not in visite:
                    pile.append(voisin)
            print(f"Voisins de {sommet}: {E[sommet]}")
            
    return {"ordre de parcours":ordre_parcours,"Noeuds visités":visite}


if __name__ == "__main__":
    
    from search.graphes.creation_graphe.main import G
    from search.graphes.creation_graphe.simple import g
    dfs(G, "A")
    print("\n")
    print(dfs_simple(g, "a"))