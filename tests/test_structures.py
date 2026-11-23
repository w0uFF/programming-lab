import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lab.structures import BoundedQueue, Stack


class StructureTests(unittest.TestCase):
    def test_stack_last_in_first_out(self):
        stack = Stack()
        stack.push("one")
        stack.push("two")
        self.assertEqual(stack.pop(), "two")
        self.assertEqual(stack.pop(), "one")
        with self.assertRaises(IndexError):
            stack.pop()

    def test_bounded_queue(self):
        queue = BoundedQueue(2)
        queue.enqueue(1)
        queue.enqueue(2)
        with self.assertRaises(OverflowError):
            queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)


if __name__ == "__main__":
    unittest.main()
