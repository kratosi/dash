import graph

def topo(v, visited):

    for u in v.get_adjacent_vertices():
        if u.id not in visited:
            topo(u, visited)

    visited.append(v.id)
    print v.id, " ",


def sort(g):
    visited = []
    for v in g.get_all_vertices():
        if v.id not in visited:
            topo(v, visited)

g = graph.Graph()
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'F')
g.add_edge('D', 'F')

sort(g)
