import sys, os

sys.path.append(os.path.abspath("../creation_graphe"))

from main import g

def dfs(graphe, start, visite=None):
    
    if visite == None:
        visite = set()
    visite.add(start)
    print(f"Noeud {start}")
    print(f"voisins de {start}: ", graphe[start])
    for voisin in graphe[start]:
        if voisin not in visite:
            dfs(graphe, voisin, visite)

dfs(g, "A")