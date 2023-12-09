import heapq


with open("degerler.txt", "r") as f:
    content = f.readlines()


adj_matrix = []
for i in range(len(content)):
    adj_matrix.append([int(x) for x in content[i].split()])


edge_count = sum([sum(row) for row in adj_matrix]) // 2

def dijkstra(adj_matrix, start):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    parent = [-1] * n
    heap = [(0, start)]
    while heap:
        (distance, current) = heapq.heappop(heap)
        if visited[current]:
            continue
        visited[current] = True
        for neighbor, weight in enumerate(adj_matrix[current]):
            if weight > 0:
                distance = distances[current] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = current 
                    heapq.heappush(heap, (distance, neighbor))
    return distances, parent

start_node = 0

distances, parent = dijkstra(adj_matrix, start_node)


for i in range(len(distances)):
    if i == start_node:
        print(f"Düğüm {i} : Başlangıç düğümü")
    elif distances[i] == float('inf'):
        print(f"Düğüm {i} : Ulaşılamaz")
    else:
        path = []
        node = i
        while node != start_node:
            path.append(node)
            node = parent[node]
        path.append(start_node)
        path.reverse()
        print(f"Düğüm {i} : Uzaklık = {distances[i]}, Yol = {path}")
