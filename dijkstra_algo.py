# DIJKSTRA's ALGORITHM
# Finds the shortest path from a vertex to another in a connected, weighted graph.

# variables:
#   dict - to store the distances [vertex: distance]
#   unvisited set - holds all the unvisited vertices initailly, exception where the first vertex will not be in here!!
#   curr variable - which is the current vertex we're checkign on
# pseudocode:
# 1. assign every node an infinity distance value but set 0 to our initial vertex.
# 2. set the initial node as curr. And all other nodes are unvisited by adding all unvisited vertices in a set
# 3. for each neighbor, calulat the distance.
#  - Compare the new distance to the current assigned value and remove from unvisited set.
#  - Note that the visited vertex will never be checked again 
# 4. Once we've considered all neighbors of the curr vertex
#  - mark curr as visited
#  - remove from unvisited set
# 5. If the destination node has already been visited || if the smallest tentative distance is among the nodes in the unvisited
#   set is infinity, then STOP! The algorithm has already finished
# 6. Select the unvisited node wth the smallest distance and reassign curr to become that new node
# 7. Go back to step 3.
