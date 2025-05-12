function breadthFirstSearch(graph: Map<number, number[]>, start: number): number[] {
  const visited: Set<number> = new Set();
  const queue: number[] = [start];
  const result: number[] = [];

  while (queue.length > 0) {
    const vertex = queue.shift()!;
    if (!visited.has(vertex)) {
      visited.add(vertex);
      result.push(vertex);
      const neighbors = graph.get(vertex) || [];
      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          queue.push(neighbor);
        }
      }
    }
  }

  return result;
}

function dfsRecursive(
  graph: Record<string, string[]>,
  start: string,
  visited: Set<string> = new Set()
): void {
  visited.add(start);
  process.stdout.write(start + ' ');

  for (const neighbor of graph[start]) {
    if (!visited.has(neighbor)) {
      dfsRecursive(graph, neighbor, visited);
    }
  }
}

console.log("\nDFS (recursive) starting from A:");
dfsRecursive(graph, "A"); 

function dfsIterative(graph: Record<string, string[]>, start: string): void {
  const visited = new Set<string>();
  const stack: string[] = [start];

  while (stack.length > 0) {
    const node = stack.pop()!;
    if (!visited.has(node)) {
      visited.add(node);
      process.stdout.write(node + ' ');

      const neighbors = graph[node].slice().reverse();
      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          stack.push(neighbor);
        }
      }
    }
  }
}