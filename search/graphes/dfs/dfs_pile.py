from collections import deque

def dfs(graphe, start):
    visite = set()
    pile = deque([start])
    
    while pile:
        # prendre le dernier element (a la différence de popleft() pour la file)
        sommet = pile.pop()
        
        if sommet not in visite:
            
            print(f"Noeud {sommet}")
            
            visite.add(sommet)
            
            for voisin in graphe[sommet]:
                if voisin not in visite:
                    pile.append(voisin)
            
            print(f"Voisins de {sommet}: {graphe[sommet]}")
            
if __name__ == "__main__":
    
    from search.graphes.creation_graphe.main import G

    dfs(G, "A")
