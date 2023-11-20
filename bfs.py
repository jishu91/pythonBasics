from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C':['A'],
    'D':['B'],
    'E':['C']
}

def bfs(graph, start):
    visited = []
    queue = deque([start])  

    while queue:
        vertex = queue.popleft()  
        if vertex not in visited:
            visited.append(vertex)
            neighbours = set(graph[vertex])
            queue.extend(neighbours - set(visited))

    return visited
print(bfs(graph, 'A'))
