
from ast import literal_eval as make_tuple

class Vertex:

    def __init__(self, v):
        self.name = v
        self.neighbors = set()

    def add_neighbor(self, v):
        # print("adding neighbor:" + str(v.name))
        self.neighbors.add(v)


class Graph:
    vertices = {}
    edges = {}
    num_vertices = 0
    num_edges = 0

    def add_vertex(self, vertex):
        '''Given input should already be a vertex object'''
        self.vertices[vertex.name] = []         # {'1': []}
        self.num_vertices += 1

    def add_edge(self, u, v, cost=0):
        # makes sure it's in the dictionary before adding it
        if u.name in self.vertices and v.name in self.vertices:
            # go through the vertices to get to the vertex of u and v

            u_vert = self.vertices[u.name]          # gives the array
            v_vert = self.vertices[v.name]          # gives the array

            u_vert.append(v.name)
            v_vert.append(u.name)

            u.add_neighbor(v)
            v.add_neighbor(u)

            self._add_path(u, v, cost)

    def _add_path(self, u, v, weight=0):
        if u in self.edges:
            # adding another tuple to the array that contains the direction to the other vertex and it's weight
            self.edges[u].append((v, weight))
        else:
            # creating a new array of where u points to v with a weight
            self.edges[u] = [(v, weight)]
        self.num_edges += 1

    def print_graph(self):
        # print("# Vertices: " + str(self.num_vertices))
        # print("# Edges: " + str(self.num_edges))

        print("# Vertices: " + str(len(self.vertices)))
        print("# Edges: " + str(len(self.edges)))

        print("Edge List:")
        for key in self.edges:              # self.edges = dictionary where key is vertex object, and value is array of tuple
            # self.edges[key] gives us the value which is already a tuple.
            array_tup = self.edges[key]     # ex. [(v_to, weight)]
            for tup in array_tup:           # ex. (v_to, weight)
                print((key.name, tup[0].name, tup[1]))

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertices.values())



def main():
    graph = Graph()

    with open('graph_data.txt', 'r') as file:
        lines = file.readlines()

        for x in lines:
            if x[0].isalpha():
                continue
            if x[0].isdigit():          # making sure this is the line with all the vertices
                # create Graph by looping through the line that contains all the vertices
                for key in x.strip().split(","):     # key is 1, 2, 3, 4
                    graph.add_vertex(Vertex(key))
            else:
                # is the neighbors of the vertex at str[0]
                tuple__neighbors = make_tuple(x)        # tuple__neighbors is (1,2,10)
                v_from = Vertex(str(tuple__neighbors[0]))
                v_to = Vertex(str(tuple__neighbors[1]))
                weight = tuple__neighbors[2]

                graph.add_edge(v_from, v_to, weight)

        # loop through the pointers and call add_edge from the first v to the second v
        return graph.print_graph()

if __name__ == '__main__':
    main()
