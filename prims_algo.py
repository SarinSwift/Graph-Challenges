
# PRIM's ALGORITHM

# variables:
#   set S - to store the vertices, where starts off empty.
# pseudocode:
# 1. select a random vertex from the graph, and add it to S
# 2. loop through every adjacent vertex in S,
    # find the adjacent vertices and then calculate the distance from the given v to the distanced vertex
    # don't forget to discard the vertex if already in S
# 3. Add nearest vertex to S. [This means that S will contain the minimum spanning tree]
# 4. Repeat steps 2, and 3 until S len is the same as all number of vertices in the graph!
