import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    print(dijkstra(graph, 'A'))
