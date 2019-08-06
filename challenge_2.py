
import sys
import queue
from ast import literal_eval as make_tuple

# Update your Graph ADT code to use Breadth-first search to compute the shortest path
# between two provided vertices in your graph.
# example of calling: python3 challenge_2.py graph_data.txt 1 5

class Vertex:

    def __init__(self, v):
        self.name = v
        self.neighbors = set()
        self.parent = None

    def add_neighbor(self, v):
        # print("adding neighbor:" + str(v.name))
        self.neighbors.add(v)


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        '''Given input should already be a vertex object'''
        self.vertices[vertex.name] = vertex         # {vertex name: vertex}

    def add_edge(self, from_vert, to_vert):
        if from_vert.name in self.vertices and to_vert.name in self.vertices:
            from_vert.add_neighbor(to_vert)
            to_vert.add_neighbor(from_vert)

    def bfs(self, from_vert, to_vert):

        '''
        properties needed:
            queue - to store the current nodes and add in it's neighbors
            seen set - to store all the seen vertices
            path array - has the shortest path from 'from_vert' > 'to_vert'

        pseudocode:
            - start by adding from_vert to the q
            - loop through the q while it's not nil
                - pop the item off q and store it in a variable (curr)
                - add curr to the seen set
                - loop through all of curr's neighbor
                    - add the neighbor to the q only if it hasn't been seen
                    - and set our neighbor's parent variable to be curr (this let's us keep track of vertices in the form of a tree)
                    - if neighbor is 'to_vert', we want to break out of the loop

            - once we set neighbors parent we can do a loop to go up the tree
            - create a variable called 'node' that starts at the 'to_vert'
            - loop while node is not nil
                - add node to the path array
                - update node to be the node's parent (this means we're going up the tree)

            - we can return the path array in reverse order! So it starts at 'from_vert' to 'to_vert'
        '''

        q = queue.Queue()       # where we perform bfs
        seen = set()            # keeps track of seen vertices
        path = []               # the path of vertices from from_vert to to_vert

        q.put(from_vert)

        while q:
            # print("q is", list(q.queue))
            curr = q.get()
            seen.add(curr)

            if curr == to_vert:         # if we get to the expected vertex, we can break out of the for loop
                break

            # print("getting neighbors of curr:", curr.neighbors)
            for nei in curr.neighbors:
                if nei not in seen:
                    q.put(nei)
                    nei.parent = curr
                if nei == to_vert:
                    break

        node = to_vert
        while node:
            path.append(node.name)
            node = node.parent

        # print("path isss", path[::-1])
        return path[::-1]

    def print_graph(self):

        print("# Vertices: " + str(len(self.vertices)))


    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertices.values())

# def read_graph_file():
#


def main():

    text_file = sys.argv[1]
    from_vert = sys.argv[2]
    to_vert = sys.argv[3]

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

                # Make sure we're grabbing the correct vertex by getting it from the populated graph's
                v_from = graph.vertices[str(tuple__neighbors[0])]
                v_to = graph.vertices[str(tuple__neighbors[1])]

                # v_from = Vertex(str(tuple__neighbors[0]))
                # v_to = Vertex(str(tuple__neighbors[1]))
                # print(v_from)
                graph.add_edge(v_from, v_to)

        # print("main, graph.vertices: ", graph.vertices)
        # print("main, graph.vertices object 1: ", list(graph.vertices['1'].neighbors))

    return print(graph.bfs(graph.vertices[from_vert], graph.vertices[to_vert]))

if __name__ == '__main__':
    main()
