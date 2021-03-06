import unittest
from graph import *


class StructTest(unittest.TestCase):
    def setUp(self):

        self.graph_to_test = Graph()
        self.graph_to_test.add_edge(1, 4)
        self.graph_to_test.add_edge(1, 2)
        self.graph_to_test.add_edge(1, 3)
        self.graph_to_test.add_edge(4, 5)
        self.graph_to_test.add_edge(5, 6)
        self.graph_to_test.add_edge(6, 7)
        self.graph_to_test.add_edge(7, 8)
        self.graph_to_test.add_edge(8, 10)
        self.graph_to_test.add_edge(3, 9)
        self.graph_to_test.add_edge(9, 10)
        self.graph_to_test.add_edge(2, 8)

    def test_adj_list(self):
        self.assertEqual(dict(self.graph_to_test.adjacency_list),
                         {1: [4, 2, 3],
                          4: [5],
                          5: [6],
                          6: [7],
                          7: [8],
                          8: [10],
                          3: [9],
                          9: [10],
                          2: [8]})

    def test_find_mother(self):
        self.assertEqual(self.graph_to_test.find_mother(), 1)

    def test_dfs(self):
        self.assertEqual(self.graph_to_test.dfs(),
                         [10, 8, 7, 6, 5, 4, 2, 9, 3, 1])


if __name__ == '__main__':
    unittest.main()
