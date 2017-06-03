import graph


def bfs(g):
    visited = []
    for vertex in g.get_all_vertices():
        if vertex.id not in visited:
            queue = [vertex]

            while queue:
                vertex = queue.pop(0)
                print vertex.id , " ",
                visited.append(vertex.id)

                for adj_vertex in vertex.get_adjacent_vertices():
                    queue.append(adj_vertex)


g = graph.Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'H')
g.add_edge('C', 'E')
g.add_edge('E', 'F')

bfs(g)
