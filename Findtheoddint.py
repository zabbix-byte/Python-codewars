'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
[0, 0, 6, 0, 6, 3, 3, 3, 3] should return 0, because it appears 1 time (which is odd).
'''
import unittest


def find_it(seq):
    hash = {}

    for i in seq:
        if hash.get(i) is None:
            hash[i] = 1
            continue

        hash[i] += 1

    for i in hash:
        if hash[i] % 2 != 0:
            return i


class TestFindIt(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(
            find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

    def test_2(self):
        self.assertAlmostEqual(
            find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1)

    def test_3(self):
        self.assertAlmostEqual(
            find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5)

    def test_4(self):
        self.assertAlmostEqual(find_it([10]), 10)

    def test_5(self):
        self.assertAlmostEqual(find_it([10, 10, 10]), 10)

    def test_6(self):
        self.assertAlmostEqual(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10)

    def test_7(self):
        self.assertAlmostEqual(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1)


if __name__ == '__main__':
    unittest.main()
