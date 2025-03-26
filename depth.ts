type Graph = {
  [node: string]: string[];
};


function dfs(graph: Graph, start: string): string[] {
  const visited = new Set<string>();
  const stack: string[] = [start];
  const result: string[] = [];

  visited.add(start);
  stack.push(start);

  while (stack.length > 0) {
    const current = stack.pop();

    if (!visited.has(current)) {
      visited.add(current);
      result.push(current);

      for (const neighbor of graph[current]) {
        if (!visited.has(neighbor)) {
          stack.push(neighbor);
        }
      }
    }
  }

  return result;
}

// function dfs(
//   graph: Graph,
//   start: string,
//   visited: Set<string> = new Set(),
//   result: string[] = []
// ): string[] {
//   visited.add(start);
//   result.push(start);

//   for (const neighbor of graph[start]) {
//     if (!visited.has(neighbor)) {
//       dfs(graph, neighbor, visited, result);
//     }
//   }

//   return result;
// }


const graph: Graph = {
  A: ["B", "C"],
  B: ["A", "D", "E"],
  C: ["A", "F"],
  D: ["B"],
  E: ["B", "F"],
  F: ["C", "E"]
};

const dfsIterativeOrder = dfs(graph, "A");
console.log("DFS (Iterative) Order:", dfsIterativeOrder);