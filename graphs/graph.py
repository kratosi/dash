class Vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
        self.adjacent = []

    def add_adjacent_vertex(self, u):
        self.adjacent.append(u)

    def get_adjacent_vertices(self):
        return self.adjacent


class Graph:
    def __init__(self):
        self.undirected = False
        self.vertices = {}

    def get_all_vertices(self):
        return self.vertices.values()

    def add_edge(self, vertex1, vertex2):
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
