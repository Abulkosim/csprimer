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
        
