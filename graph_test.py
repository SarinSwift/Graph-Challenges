import unittest
from challenge_1 import Graph
from challenge_1 import Vertex

class GraphTest(unittest.TestCase):
    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex("apple")
        graph.add_vertex("banana")

        self.assertEqual(2, graph.num_vertices)
        # self.assertIsInstance(graph.get_vertex("apple"), Vertex)
        self.assertIsInstance(graph.vertices["apple"], Vertex)

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex("apple")
        graph.add_vertex("banana")
        graph.add_vertex("coconut")

        graph.add_edge("apple", "banana")
        graph.add_edge("apple", "coconut", 3)

        self.assertEqual(3, graph.num_vertices)
        self.assertEqual(2, graph.num_edges)

        graph.add_edge("pineapple", "strawberry")

        self.assertEqual(5, graph.num_vertices)
        self.assertEqual(3, graph.num_edges)
        self.assertCountEqual(
            ["apple", "banana", "coconut", "pineapple", "strawberry"],
            graph.get_vertices())

class VertexTest(unittest.TestCase):
    def test_add_neighbor(self):
        vertex1 = Vertex("apple")
        vertex2 = Vertex("banana")
        vertex3 = Vertex("coconut")

        vertex1.add_neighbor(vertex2)
        vertex1.add_neighbor(vertex3, 3)

        self.assertEqual(2, len(vertex1.neighbors))
        self.assertEqual(0, vertex1.neighbors[vertex2])
        self.assertEqual(3, vertex1.neighbors[vertex3])

if __name__ == "__main__":
    unittest.main()
