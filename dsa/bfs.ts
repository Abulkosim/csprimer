type TreeNode<T> = {
  val: T;
  left: TreeNode<T> | null;
  right: TreeNode<T> | null;
}

function bfsLevelOrder<T>(root: TreeNode<T> | null): T[] {
  if (!root) return [];

  const result: T[] = [];
  const queue: Array<TreeNode<T>> = [root];

  while (queue) {
    const node = queue.shift();
    if (!node) break;
    
    result.push(node.val);

    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
  
  return result;  
}

