
import sys
import queue
from ast import literal_eval as make_tuple

# Update your Graph ADT code to use Breadth-first search to compute the shortest path
# between two provided vertices in your graph.
# example of calling: python3 challenge_2.py graph_data.txt 1 5

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

        # ANOTHER WAY OF BFS FOR SHORTEST PATH
        # path_found = False
        # q = queue.Queue()       # where we perform bfs
        # visited = set()            # keeps track of seen vertices
        # path = []               # the path of vertices from from_vert to to_vert
        #
        # # add in 'from_vert' as a vertex object and then insert it to the qeueu
        # curr = self.get_vertex(from_vert)
        # curr.parent = None
        # q.put(curr)
        # visited.add(curr)
        #
        # while q:
        #     curr = q.get()
        #
        #     if curr.name == to_vert:
        #         path_found = True
        #         break
        #
        #     for neighbor in curr.neighbors:
        #         if neighbor.name not in visited:
        #             q.put(neighbor)
        #             visited.add(neighbor)
        #             neighbor.parent = curr
        #
        # if path_found:
        #     curr = self.get_vertex(to_vert)
        #     while curr is not None:
        #         path.append(curr.name)
        #         curr = curr.parent
        #     return path[::-1]
        # else:
        #     print("No available routes from these locations!")

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

    # grabing the name of the vertex 
    a_name = sys.argv[2]
    b_name = sys.argv[3]
    # grabing the vertex object
    a = g.vertices[a_name]
    b = g.vertices[b_name]

    # use bfs to compute shortest path
    print(g.bfs(a, b))

if __name__ == '__main__':
    main()
