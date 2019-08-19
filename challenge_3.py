import sys
import queue
from ast import literal_eval as make_tuple

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
    vertices = {}

    def add_vertex(self, name):
        '''Given input is the name of the vertex'''
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


    def is_connected_iterative(self, vertex):
        '''
        properties needed:
            visited set - to store all the vertices passed while traversing the graph
            stack - to keep track of our trace with vertices that are connected
        pseudocode:
            - add the curr vertex in our 'stack' set
            - loop through the stack while it's not empty
                - pop a vertex off the stack and call it 'curr'
                - make sure 'curr' is not already in visited
                    - add the curr into our visited set
                    - loop through the curr's neighbor
                    - push all the neighbors on to our stack
            - once our stack is empty, this means that we have looped through all of our connections,
              and we can return the visited set
        '''
        visited = set()
        stack = stack()
        stack.push(vertex)

        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for neighbor in vertex.neighbors:
                    stack.push(neighbor)
        return visited


    def is_connected_recursive(self, vertex, visited=None):
        '''
        properties needed:
            visited set - to store all the vertices passed while traversing the graph
        pseudocode:
            - add the curr vertex in our 'visited' set
            - loop through neighbors of the curr vertex
                - call the recursive function on it's neighbor with the same visited set
            - after looping through all of the connected paths, the visited set will contain all the vertices that we
              have traversed through from the dfs function
        '''
        if visited == None:
            visited = set()

        visited.add(vertex)
        for neighbor in vertex.neighbors:
            is_connected(neighbor, visited)

        return len(visited) == len(self.vertices)

    def dfs_iterative(self, from_vert, to_vert):
        '''
        we use the stack to yeild the each possible path to get to our end goal vertex
        properties needed:
            visited set - to store all the vertices passed while traversing from 'from_vert' to 'to_vert'
            stack - to keep track of our trace with vertices that are connected
        pseudocode:
            - start off with our stack containing the 'from_vert'
            - loop through the stack while not empty
                - pop off the stack and store in a variabel called 'curr'
                - if 'curr' is not in our visited set,
                    - add curr to visited set
                    - loop through curr's neighbors
                        - add the neighbor on to the stack
            - retrun our visited set of vertices through the path
        '''
        visited = set()
        stack = stack()
        stack.push(from_vert)

        while stack:
            curr = stack.pop()
            if curr == to_vert:
                break
            if curr not in visited:
                visited.add(curr)
                for neighbor in curr.neighbors:
                    stack.push(neighbor)

        return visited


    def dfs_recursive(self, from_vert, to_vert, visited=None):
        '''
        properties needed:
        pseudocode:
        '''
        # initializing the seen array
        if visited == None:
            visited = set()

        if from_vert == to_vert:
            # might need to append from_vert in here first!!!
            return visited

        if from_vert not in visited:
            visited.add(from_vert)
            for neighbor in from_vert.neighbors:
                self.dfs_recursive(neighbor, to_vert, visited)

        print(list(visited))
        return list(visited) is not None

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
    if a_name in g.vertices and b_name in g.vertices:
        a = g.vertices[a_name]
        b = g.vertices[b_name]
    else:
        a = None
        b = None
        print("Error: No vertex with that given item in the graph")
        return False

    # returns True if there's a path between these vertices
    print(g.dfs_recursive(a, b))


if __name__ == '__main__':
    main()
