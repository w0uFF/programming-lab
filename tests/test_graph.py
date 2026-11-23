import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lab.graph import breadth_first, shortest_path


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

    def test_breadth_first(self):
        self.assertEqual(breadth_first(self.graph, "A"), ["A", "B", "C", "D"])

    def test_path(self):
        self.assertEqual(shortest_path(self.graph, "A", "D"), ["A", "B", "D"])

    def test_unreachable(self):
        self.assertIsNone(shortest_path(self.graph, "D", "A"))


if __name__ == "__main__":
    unittest.main()
