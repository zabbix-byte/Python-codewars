'''
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
'''
import unittest


def summation(num):
    return sum(range(1, num+1))


class TestSummation(unittest.TestCase):
    def test_summations(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)
        self.assertEqual(summation(22), 253)
        self.assertEqual(summation(100), 5050)
        self.assertEqual(summation(213), 22791)


if __name__ == '__main__':
    unittest.main()
