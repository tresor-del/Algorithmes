
def dfs_simple(G, v):
    V, E = G
    visite  = set()
    sommets = []

    def parcours(u):
        if u not in visite:
            visite.add(u)
            
            print(f"Noeud {u}")
            print(f"voisins de {u}: ", E[u])
            
            for v in E[u]:
                parcours(v)

            sommets.append(u)

    parcours(v)

    return sommets

def dfs(G, start, visite=None):
    
    if visite == None:
        visite = set()
    visite.add(start)
    
    print(f"Noeud {start}")
    print(f"voisins de {start}: ", G[start])
    
    for voisin in G[start]:
        if voisin not in visite:
            dfs(G, voisin, visite)

# Exemples
if __name__ == "__main__":

    
    from search.graphes.creation_graphe.main import G
    from search.graphes.creation_graphe.simple import g

    print("Parcours graphe: \n")
    dfs(G, "A")
    print("\n")
    print("Parcours graphe simple: \n",dfs_simple(g, "e"))