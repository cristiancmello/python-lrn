import unittest

from kata_1.stack import Stack, Underflow


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_can_create_stack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_after_one_push_will_not_empty(self):
        self.stack.push(0)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

    def test_after_one_push_and_one_pop_will_empty(self):
        self.stack.push(0)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_after_two_pushes_size_is_two(self):
        self.stack.push(0)
        self.stack.push(0)
        self.assertEqual(self.stack.size(), 2)

    def test_popping_empty_stack_raises_underflow(self):
        with self.assertRaises(Underflow):
            self.stack.pop()

    def test_after_pushing_x_will_pop_x(self):
        self.stack.push(99)
        self.assertEqual(self.stack.pop(), 99)
        self.stack.push(88)
        self.assertEqual(self.stack.pop(), 88)

    def test_after_pushing_x_and_y_will_pop_y_then_x(self):
        self.stack.push(99)
        self.stack.push(88)
        self.assertEqual(self.stack.pop(), 88)
        self.assertEqual(self.stack.pop(), 99)
