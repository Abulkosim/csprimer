def dfs_rec(t):
    if t is None:
        return

    print(t.val)
    dfs_rec(t.left)
    dfs_rec(t.right)


def dfs(t):
    stack = [t]

    while stack:
        node = stack.pop()
        if node is None:
            continue

        print(node.val)
        stack.append(node.right)
        stack.append(node.left)


def dfs_graph_rec(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_graph_rec(graph, neighbor, visited)


def dfs_graph(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in graph[start]:
                if neighbor not in visited:
                    stack.append(neighbor)

                    # Example usage


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
