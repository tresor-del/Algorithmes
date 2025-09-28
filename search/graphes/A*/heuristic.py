import heapq


def astar(graph, start, goal, h):
    # g = coût depuis le départ
    g = {node: float('inf') for node in graph}
    g[start] = 0
    
    # f = g + heuristique
    f = {node: float('inf') for node in graph}
    f[start] = h(start, goal)
    
    heap = [(f[start], start)]
    
    came_from = {}  # pour reconstruire le chemin
    
    while heap:
        _, current = heapq.heappop(heap)
        
        if current == goal:
            # reconstruction du chemin
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g[goal], f
        
        for neighbor, weight in graph[current].items():
            tentative_g = g[current] + weight
            if tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = tentative_g + h(neighbor, goal)
                heapq.heappush(heap, (f[neighbor], neighbor))
    
    return None, float('inf')



if __name__ == "__main__":
    
    G = {
        "A": {"B": 2, "C": 5},
        "B": {"A": 2, "C": 1, "D": 4},
        "C": {"A": 5, "B": 1, "D": 2},
        "D": {"B": 4, "C": 2}
    }
    
    # heuristique simplifiée : nombre de lettres différentes (juste pour exemple)
    def h(node, goal):
        return abs(ord(goal) - ord(node))

    path, cost, f= astar(G, "A", "D", h)
    print("Chemin:", path)
    print("Coût:", cost)
    print("f: ", f)