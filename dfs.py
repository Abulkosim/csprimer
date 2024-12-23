class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root, target):
    if root is None:
        return

    if root.value == target:
        return True
    dfs(root.left, target)
    dfs(root.right, target)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    result = dfs(root, 5)
