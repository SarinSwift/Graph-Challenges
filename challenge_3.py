

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
            return visited

        if from_vert not in visited:
            visited.add(from_vert)
            print(from_vert)
            for neighbor in from_vert.neighbors:
                dfs_recursive(neighbor, to_vert, visited)

        return visited

    def __iter__(self):
        """
        iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vertices.values())

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
