def bfs(graph, start):
    visited = set()
    queue = []
    
    queue.append(start)
    visited.add(start)
    
    while queue:
        vertex = queue.pop(0)
        
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
