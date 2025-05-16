class dfs:
    def dfs1(self, graph, root, visited= None):
        if not visited:
            visited = set()
        visited.add(root)

        for nbr in graph.get(root, []):
            if nbr not in visited:
                self.dfs1(graph, nbr,visited)

        return visited
d= dfs()
# Example graph represented as an adjacency list
graph_dfs = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H']

}

res = d.dfs1(graph_dfs, 'C')
print(res)