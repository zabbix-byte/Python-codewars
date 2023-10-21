'''
Code as fast as you can! You need to double the integer and return it.
'''

import unittest


def double_integer(i):
    return i * 2


class TestDoubleIntegerFunc(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(double_integer(2), 4)
        self.assertEqual(double_integer(4), 8)
        self.assertEqual(double_integer(-10), -20)
        self.assertEqual(double_integer(0), 0)
        self.assertEqual(double_integer(100), 200)


if __name__ == '__main__':
    unittest.main()
