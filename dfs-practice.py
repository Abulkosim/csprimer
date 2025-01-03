def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    print("\nDFS (recursive) starting from A:")
    dfs_recursive(graph, 'A')  
    
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  
        if node not in visited:
            visited.add(node)
            print(node, end=' ')

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

if __name__ == "__main__":
    print("\nDFS (iterative) starting from A:")
    dfs_iterative(graph, 'A')  