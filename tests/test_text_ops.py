import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lab.text_ops import normalize_spaces, words, is_palindrome, rotate_ascii


class TextTests(unittest.TestCase):
    def test_whitespace(self):
        self.assertEqual(normalize_spaces(" a  \n b "), "a b")

    def test_words(self):
        self.assertEqual(words("Hello, HELLO!"), ["hello", "hello"])

    def test_palindrome(self):
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertFalse(is_palindrome("Data structures"))

    def test_rotation(self):
        self.assertEqual(rotate_ascii("Zoo-ABC", 1), "App-BCD")


if __name__ == "__main__":
    unittest.main()
