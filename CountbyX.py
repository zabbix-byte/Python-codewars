'''
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
'''

import unittest


def count_by(x, n):
    return [x*i for i in range(1, n+1)]


class TestCountBy(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(count_by(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(count_by(2, 5), [2, 4, 6, 8, 10])
        self.assertEqual(count_by(3, 5), [3, 6, 9, 12, 15])
        self.assertEqual(count_by(50, 5), [50, 100, 150, 200, 250])
        self.assertEqual(count_by(100, 5), [100, 200, 300, 400, 500])


if __name__ == '__main__':
    unittest.main()
