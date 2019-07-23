
import sys
import queue

# Update your Graph ADT code to use Breadth-first search to compute the shortest path
# between two provided vertices in your graph.
# example of calling: python3 challenge_2.py graph_data.txt 1 5

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
    seen = Set()            # keeps track of seen vertices
    path = []               # the path of vertices from from_vert to to_vert

    q.push(from_vert)

    while q:
        curr = q.pop()
        seen.add(curr)

        for nei in curr.get_neighbors():
            if nei not in seen:
                q.push(nei)
                nei.parent = curr
            if nei == to_vert:
                break

    node = to_vert
    while node:
        path.append(node)
        node = node.parent

    return path.reverse()


def main():
    text_file = sys.argv[1]
    from_vert = sys.argv[2]
    to_vert = sys.argv[3]




if __name__ == '__main__':
    main()
