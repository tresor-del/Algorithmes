from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])        # On met le point de départ dans la file
    while queue:
        vertex = queue.popleft()  # On prend le premier nœud de la file
        if vertex not in visited:
            print(vertex)         # On traite ce nœud
            visited.add(vertex)   # On marque comme visité
            queue.extend(graph[vertex])  # On ajoute tous ses voisins à la file
