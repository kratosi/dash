"""
kruskal algorith finds the minimum spanning tree
"""
import graph
import disjoint_sets

def kruskal(graph):
    edges = graph.edges
    edges.sort(key=lambda x: x.weight)

    ds =  disjoint_sets.DisjointSet()

    for v in graph.get_all_vertices():
        ds.make_set(v.id)

    result = []
    for e in edges:
        v1 = e.vertex1
        v2 = e.vertex2
        set1 = ds.find_set(v1.id)
        set2 = ds.find_set(v2.id)

        if set1 == set2:
            continue

        ds.union(v1.id, v2.id)
        result.append(e)

    print result
    for r in result:
        print r.vertex1.id, r.vertex2.id, r.weight


def main():
    g = graph.Graph()
    """
    A -- 5 --> B -- 6 --> C
    |          |          |
    8          4          2
    V          V          V
    D -- 3 --> E -- 8 --> F
    """
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'D', 8)
    g.add_edge('B', 'C', 6)
    g.add_edge('B', 'E', 4)
    g.add_edge('D', 'E', 3)
    g.add_edge('E', 'F', 8)
    g.add_edge('C', 'F', 2)

    print kruskal(g)

main()
