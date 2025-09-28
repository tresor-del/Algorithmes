import networkx as nx
import matplotlib.pyplot as plt

# création d'un graphe
G = nx.DiGraph()

# ajouter des sommmets
G.add_nodes_from(["A", "B", "C", "D"])

# ajouter des arrêtes
G.add_edges_from([("A", "B"), ("B", "D"), ("D", "E"), ("B", "F"), ("A", "C"), ("C", "G")])

# dessiner le graphe
nx.draw(G, with_labels=True, node_color="lightblue", node_size=1500, font_size=12)
plt.show()

plt.savefig("graphe.png")

print("Graphe enregistré sous graphe.png")

