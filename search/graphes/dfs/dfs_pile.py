import sys, os

sys.path.append(os.path.abspath("../creation_graphe"))

from main import g

from collections import deque

def dfs(graphe, start):
    visite = set()
    pile = deque([start])
    
    while pile:
        # prendre le dernier element (a la différence de popleft() pour la file)
        vertex = pile.pop()
        
        if vertex not in visite:
            
            print(f"Noeud {vertex}")
            
            visite.add(vertex)
            
            for voisin in graphe[vertex]:
                if voisin not in visite:
                    pile.append(voisin)
            
            print(f"Voisins de {vertex}: {pile}")
            
dfs(g, "A")