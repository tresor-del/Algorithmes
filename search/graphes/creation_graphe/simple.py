# les sommets du graphe
V = {"a", "b", "c", "d", "e"}

# les arrêtes du graphe
E = {"a": ["b", "c"],
     "b": ["d", "f"],
     "c": ["g"],
     "d": ["e"],
     "e": [],
     "f": [],
     "g": []}

# création du graphe
g = (V, E)