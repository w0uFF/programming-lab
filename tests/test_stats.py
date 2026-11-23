import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lab.stats import mean, median, population_stddev


class StatsTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(mean([2, 4, 6]), 4)

    def test_median(self):
        self.assertEqual(median([7, 1, 5]), 5)
        self.assertEqual(median([3, 1, 2, 4]), 2.5)

    def test_stddev(self):
        self.assertAlmostEqual(population_stddev([2, 2, 2]), 0.0)

    def test_empty(self):
        with self.assertRaises(ValueError):
            mean([])


if __name__ == "__main__":
    unittest.main()
