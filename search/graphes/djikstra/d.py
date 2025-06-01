import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # distances initiales
    distances[start] = 0
    heap = [(0, start)]  # tas avec (distance, noeud)
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances
