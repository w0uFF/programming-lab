import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lab.math_ops import gcd, is_prime, multiples, fibonacci_terms


class MathTests(unittest.TestCase):
    def test_primes(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(91))

    def test_gcd(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(-12, 8), 4)

    def test_multiples(self):
        self.assertEqual(multiples(1, 10, 3), [3, 6, 9])
        with self.assertRaises(ValueError):
            multiples(1, 10, 0)

    def test_fibonacci(self):
        self.assertEqual(fibonacci_terms(7), [0, 1, 1, 2, 3, 5, 8])


if __name__ == "__main__":
    unittest.main()
