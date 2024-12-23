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


def dfs_iter(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
