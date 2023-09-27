import unittest

from kata_1.stack import Stack, StackUnderflowError


class TestStack(unittest.TestCase):
    def setUp(self):
        self.__stack = Stack()

    def test_can_create_stack(self):
        self.assertTrue(self.__stack.is_empty())
        self.assertEqual(0, self.__stack.size())

    def test_after_one_push_will_not_empty(self):
        self.__stack.push(0)
        self.assertFalse(self.__stack.is_empty())
        self.assertEqual(1, self.__stack.size())

    def test_after_one_push_and_one_pop_will_empty(self):
        self.__stack.push(0)
        self.__stack.pop()
        self.assertTrue(self.__stack.is_empty())
        self.assertEqual(0, self.__stack.size())

    def test_after_two_pushes_size_is_two(self):
        self.__stack.push(0)
        self.__stack.push(0)
        self.assertEqual(2, self.__stack.size())

    def test_popping_empty_stack_raises_underflow(self):
        with self.assertRaises(StackUnderflowError):
            self.__stack.pop()

    def test_after_pushing_x_will_pop_x(self):
        self.__stack.push(99)
        self.assertEqual(99, self.__stack.pop())

        self.__stack.push(88)
        self.assertEqual(88, self.__stack.pop())

    def test_after_pushing_x_and_y_will_pop_y_then_x(self):
        self.__stack.push(99)
        self.__stack.push(88)
        self.assertEqual(88, self.__stack.pop())
        self.assertEqual(99, self.__stack.pop())
