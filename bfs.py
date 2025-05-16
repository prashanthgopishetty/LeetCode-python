import collections

class bfs:
    def bef1(self, graph, root):
        visited = set()
        q = collections.deque([root])

        while q:
            vtx = q.popleft()
            if vtx not in visited:
                visited.add(vtx)
                for nbr in graph.get(vtx,[]):
                    if nbr not in visited:
                        q.append(nbr)
        return visited

b= bfs()
# Example graph represented as an adjacency list
graph_bfs = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H']

}

res = b.bef1(graph_bfs, 'C')
print(res)