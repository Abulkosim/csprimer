type DFSTreeNode<T> = {
  val: T;
  left: DFSTreeNode<T> | null;
  right: DFSTreeNode<T> | null;
}

function dfsPreorder<T>(root: DFSTreeNode<T> | null): T[] {
  if (!root) return [];

  const result: T[] = [];
  const stack: Array<DFSTreeNode<T>> = [root];

  while (stack.length) {
    const node = stack.pop();
    if (!node) break;

    result.push(node.val); 
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }

  return result;
}

function preorder<T>(root: DFSTreeNode<T> | null, out: T[] = []): T[] {
  if (!root) return out;
  out.push(root.val);
  preorder(root.left, out);
  preorder(root.right, out);
  return out;
}