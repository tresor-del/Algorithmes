import networkx as nx
import matplotlib.pyplot as plt

# crétion d'un graphe
g = nx.Graph()

# ajouter des sommmets
g.add_nodes_from(["A", "B", "C", "D"])

# ajouter des arrêtes
g.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("A", "B1"), ("B1", "C1"),("C1", "D1"), ("D1", "E1"), ("A", "B2"), ("B2", "C2"),("C2", "D2"), ("D2", "E2")])

# dessiner le graphe
nx.draw(g, with_labels=True, node_color="lightblue", node_size=1500, font_size=12)
plt.show()

plt.savefig("graphe.png")
print("Graphe enregistré sous graphe.png")
print("Voisins de B1 :", list(g.neighbors("B1")))
