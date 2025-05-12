function bfs(graph, start) {
    var visited = new Set();
    var queue = [];
    var result = [];
    visited.add(start);
    queue.push(start);
    while (queue.length > 0) {
        var current = queue.shift();
        result.push(current);
        for (var _i = 0, _a = graph[current]; _i < _a.length; _i++) {
            var neighbor = _a[_i];
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    return result;
}
var g = {
    A: ["B", "C"],
    B: ["A", "D", "E"],
    C: ["A", "F"],
    D: ["B"],
    E: ["B", "F"],
    F: ["C", "E"]
};
var bfsOrder = dfs(g, "A");
console.log("DFS (Iterative) Order:", bfsOrder);
