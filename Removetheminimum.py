'''
The museum of incredible dull things
The museum of incredible dull things wants to get rid of some exhibitions.
 Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions
   She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair,
 so she asks you to write a program that tells her the ratings of the items after one removed the lowest
   one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list.
 If there are multiple elements with the same value, remove the one with a lower index
 . If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
'''

import unittest
import copy
from numpy.random import randint


def remove_smallest(numbers):
    val = copy.deepcopy(numbers)

    if len(val) == 0:
        return val

    index_to_remove = 0
    current = val[0]

    for i in range(1, len(val)):
        if val[i] < current:
            current = val[i]
            index_to_remove = i

    del val[index_to_remove]

    return val


class TestRemoveSmallest(unittest.TestCase):
    def test_case(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [
                         2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [
                         5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
        self.assertEqual(remove_smallest([1, 2, 3, 1, 1]), [
                         2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
        self.assertEqual(remove_smallest([]), [], "Wrong result for []")

        for i in range(10):
            x = randint(1, 400)
            self.assertEqual(remove_smallest([x]), [], "Wrong result for [{}]".format(x))

if __name__ == '__main__':
    unittest.main()
