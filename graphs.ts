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
