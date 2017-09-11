class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.adjacent = []

    def add_adjacent_vertex(self, u):
        self.adjacent.append(u)

    def get_adjacent_vertices(self):
        return self.adjacent


class Edge(object):
    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertex1 = vertex1
        self.vertex2 = vertex2


class Graph:
    def __init__(self):
        self.undirected = False
        self.vertices = {}
        self.edges = []

    def get_all_vertices(self):
        return self.vertices.values()

    def add_edge(self, vertex1, vertex2, weight=0):
        v1 = self.vertices.get(vertex1)
        if not v1:
            v1 = Vertex(vertex1)
            self.vertices[vertex1] = v1

        v2 = self.vertices.get(vertex2)
        if not v2:
            v2 = Vertex(vertex2)
            self.vertices[vertex2] = v2

        v1.add_adjacent_vertex(v2)
        if self.undirected:
            v2.add_adjacent_vertex(v1)

        e = Edge(v1, v2, weight)
        self.edges.append(e)
