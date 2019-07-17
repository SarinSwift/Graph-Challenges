
from ast import literal_eval as make_tuple

class Vertex:

    def __init__(self, v):
        self.name = v
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.add(v)


class Graph:
    vertices = {}
    num_vertices = 0
    num_edges = 0

    def add_vertex(self, vertex):
        '''Given input should already be a vertex object'''
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            self.num_vertices += 1

    def add_edge(self, u, v):
        # makes sure it's in the dictionary before adding it
        if u in self.vertices and v in self.vertices:
            # go through the vertices to get to the vertex of u and v
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            self.num_edges += 1

    def print_graph(self):
        print("# Vertices: " + str(self.num_vertices))
        print("# Edges: " + str(self.num_edges))
        print("Edge List:")
        for key in self.vertices.keys():
            print(key, self.vertices[key].neighbors)



def main():
    graph = Graph()

    with open('graph_data.txt', 'r') as file:
        lines = file.readlines()

        for x in lines:
            if x[0].isalpha():
                continue
            if x[0].isdigit():          # making sure this is the line with all the vertices
                # create Graph by looping through the line that contains all the vertices
                for char in x:          # x is "1, 2, 3, 4"
                    if char.isdigit():
                        graph.add_vertex(Vertex(char))
            else:
                # is the neighbors of the vertex at str[0]
                tuple__neighbors = make_tuple(x)
                v = tuple__neighbors[0]
                u = tuple__neighbors[1]
                weight = tuple__neighbors[2]
                graph.add_edge(v, u)


        # loop through the pointers and call add_edge from the first v to the second v
        return graph.print_graph()

if __name__ == '__main__':
    main()
