type GraphType = {
  [node: string]: string[];
};

function bfs(graph: Graph, start: string): string[] {
  const visited = new Set<string>();
  const queue: string[] = [];
  const result: string[] = [];

  visited.add(start);
  queue.push(start);

  while (queue.length > 0) {
    const current = queue.shift(); 
    result.push(current);

    for (const neighbor of graph[current]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }

  return result;
}


const g: GraphType = {
  A: ["B", "C"],
  B: ["A", "D", "E"],
  C: ["A", "F"],
  D: ["B"],
  E: ["B", "F"],
  F: ["C", "E"]
};

const bfsOrder = dfs(g, "A");
console.log("DFS (Iterative) Order:", bfsOrder);