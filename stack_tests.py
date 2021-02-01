import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
#from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_is_empty(self):
        stack = Stack(3)
        stack.push(7)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_is_full(self):
        stack = Stack(3)
        self.assertFalse(stack.is_full())
        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertTrue(stack.is_full())
        stack.pop()
        self.assertFalse(stack.is_full())

    def test_push_pop_peek(self):
        stack = Stack(3)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)
        stack.push(0)
        self.assertEqual(stack.peek(), 0)
        self.assertEqual(stack.pop(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)
        stack.push(1)
        stack.push(2)
        self.assertRaises(IndexError, stack.push, 3)

    def test_size(self):
        stack = Stack(3)
        self.assertEqual(stack.size(), 0)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 3)

if __name__ == '__main__':
    unittest.main()

