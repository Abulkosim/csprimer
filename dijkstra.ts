type WeightedGraph = {
  [node: string]: Array<{
    neighbor: string; 
    weight: number;
  }>;
};

const WeightedGraph: WeightedGraph = {
  A: [
    { neighbor: "B", weight: 4 },
    { neighbor: "C", weight: 2 }
  ],
  B: [
    { neighbor: "A", weight: 4 },
    { neighbor: "C", weight: 1 },
    { neighbor: "D", weight: 5 }
  ],
  C: [
    { neighbor: "A", weight: 2 },
    { neighbor: "B", weight: 1 },
    { neighbor: "D", weight: 8 },
    { neighbor: "E", weight: 10 }
  ],
  D: [
    { neighbor: "B", weight: 5 },
    { neighbor: "C", weight: 8 },
    { neighbor: "E", weight: 2 }
  ],
  E: [
    { neighbor: "C", weight: 10 },
    { neighbor: "D", weight: 2 }
  ]
};

class PriorityQueue<T> {
  private items: { key: T; priority: number }[] = [];

  enqueue(key: T, priority: number) {
    this.items.push({ key, priority });
  }

  dequeue(): T | undefined {
    if (this.items.length === 0) {
      return undefined;
    }
    this.items.sort((a, b) => a.priority - b.priority);
    return this.items.shift()!.key; 
  }

  isEmpty() {
    return this.items.length === 0;
  }
}


function dijkstra(graph: WeightedGraph, start: string): { [node: string]: number } {
  const distances: { [node: string]: number } = {};
  for (const node in graph) {
    distances[node] = Infinity;
  }
  distances[start] = 0;

  const pq = new PriorityQueue<string>();
  pq.enqueue(start, 0);

  const visited = new Set<string>();

  while (!pq.isEmpty()) {
    const currentNode = pq.dequeue();
    if (currentNode === undefined) {
      break;
    }

    visited.add(currentNode);

    for (const edge of graph[currentNode]) {
      const { neighbor, weight } = edge;

      if (!visited.has(neighbor)) {
        const newDistance = distances[currentNode] + weight;

        if (newDistance < distances[neighbor]) {
          distances[neighbor] = newDistance;
          pq.enqueue(neighbor, newDistance);
        }
      }
    }
  }

  return distances;
}


const distancesFromA = dijkstra(WeightedGraph, "A");
console.log(distancesFromA);