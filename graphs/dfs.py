import graph

def dfs_util(vertex, visited):
    print vertex.id, "  ",
    visited.append(vertex.id)

    for adj_vertex in vertex.get_adjacent_vertices():
        if adj_vertex.id not in visited:
            dfs_util(adj_vertex, visited)

def dfs(g):
    visited = []
    for vertex in g.get_all_vertices():
        if vertex.id not in visited:
            dfs_util(vertex, visited)


g = graph.Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'H')
g.add_edge('C', 'E')
g.add_edge('E', 'F')

dfs(g)
