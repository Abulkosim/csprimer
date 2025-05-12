class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
