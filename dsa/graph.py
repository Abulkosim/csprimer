class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")

                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example usage:
# Create a graph:
#     1 --- 2
#     |     |
#     4 --- 3
#     |
#     5 --- 6

g = Graph()
edges = [(1, 2), (1, 4), (2, 3), (3, 4), (4, 5), (5, 6)]
for u, v in edges:
    g.add_edge(u, v)

print("DFS starting from vertex 1:")
g.dfs(1)  # Possible output: 1 4 5 6 3 2

print("\nBFS starting from vertex 1:")
g.bfs(1)  # Possible output: 1 2 4 3 5 6
