'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique
'''

import unittest


def find_uniq(arr):
    map = {}

    for i in arr:
        if i not in map.keys():
            map[i] = 1
            continue
        map[i] += 1

    for i in map:
        if map[i] == 1:
            return i


class TestFindUniq(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
        self.assertEqual(find_uniq([3, 10, 3, 3, 3]), 10)


if __name__ == '__main__':
    unittest.main()
