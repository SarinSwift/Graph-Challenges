import sys

class Vertex:

    def __init__(self, v_name):
        self.name = v_name
        self.neighbors = {}     # key: neigbor vertex object, value: weight of connecting edge
        self.parent = None

    def add_neighbor(self, v, w=0):
        '''Given input is already a vertex object.
            v: the connecting neighbor, w: the weight
        '''
        if v not in self.neighbors:
            self.neighbors[v] = w

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f"{self.name} adjacent to {[x.name for x in self.neighbors]}"

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors.keys()

    def get_edge_weight(self, vertex):
        """Return the weight of this connecting edge between self and the given vertex object."""
        return self.neighbors[vertex]


class Graph:
    vertices = {}               # key: vertex name, value: vertex object
    num_vertices = 0            # total count of vertices in the graph
    edges = {}
    num_edges = 0

    def add_vertex(self, name):
        '''Given input is the name of the vertex'''
        self.num_vertices += 1
        self.vertices[name] = Vertex(name)
        return self.vertices[name]

    def add_edge(self, name1, name2, cost=0):
        # insert the new vertex of object1 if not yet in the graph
        if name1 not in self.vertices:
            self.add_vertex(name1)
        # insert the new vertex of object2 if not yet in the graph
        if name2 not in self.vertices:
            self.add_vertex(name2)

        # now we're sure there are both vertices in the graph, we can add negihbors to both
        object1 = self.vertices[name1]
        object2 = self.vertices[name2]
        object1.add_neighbor(object2, cost)

        self.num_edges += 1

    def get_vertex(self, name):
        """Return the vertex if it exists."""
        return self.vertices[name]

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return list(self.vertices.keys())

    def get_edges_weighted(self):
        """Return the list of edges with weights, as tuples."""
        edges = []
        for v in self.vertices.values():
            for w in v.neighbors:
                edges.append((v.name, w.name, v.neighbors[w]))
        return edges

    def is_eulerian_cycle(self):
        """ Checks if this graph has a eulerian cycle. A eulerian cycle is when all vertices in the graph
        have even number of edges"""
        # loops through all the neighbor of all it's vertices in the graph
        for vertex in self.vertices:
            neighbors = self.vertices[vertex].neighbors
            # number of neighbors must be even number or else we can return false straight away
            if len(neighbors) % 2 != 0:
                return False

        return True

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertices.values())


def read_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        # make sure it's a graph
        graph_str =  lines[0].strip() if len(lines) > 0 else None
        if graph_str != "G":
            raise Exception("File must start with G.")
        # is_bidirectional = graph_or_digraph_str == "G"

        graph = Graph()

        # add the vertices from the 2nd line
        for vertex_name in lines[1].strip("() \n").split(","):
            graph.add_vertex(vertex_name)

        # add the edges by looping through the remaing lines in the file
        # the line is (1,2,10) and so on...
        for line in lines[2:]:
            # getting rid of ',' and combining all the 2/3 values together
            new_edge = line.strip("() \n").split(",")
            if len(new_edge) < 2 or len(new_edge) > 3:
                raise Exception("Lines adding edges must include 2 or 3 values")

            # Get vertices from 'new_edge' from the first index to the second.
            vertex1, vertex2 = new_edge[:2]

            # Get weight if the len of 'new_edge' is 3. If the length is not 3, weight value will be None
            weight = int(new_edge[2]) if len(new_edge) == 3 else None

            # Add edge(s)!!
            graph.add_edge(vertex1, vertex2, weight)
            graph.add_edge(vertex2, vertex1, weight)

        return graph

def main():
    # read the file from argument given
    filename = sys.argv[1]
    g = read_from_file(filename)

    # returns True if the graph has a Eulerian cyle
    if g.is_eulerian_cycle():
        print("This graph is Eulerian: TRUE")
    else:
        print("This graph is Eulerian: FALSE")


if __name__ == '__main__':
    main()
