'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
'''

import unittest


def odd(number: int) -> bool:
    return number % 2 != 0


def generate_odd_numbers(size_of_tree, last_odd) -> tuple:
    current = last_odd
    result = []
    finded = 0

    while (finded != size_of_tree):
        current += 1
        if odd(current):
            finded += 1
            result.append(current)

    return result, result[-1]


def row_sum_odd_numbers(n):
    map = []
    last_odd = 0

    for i in range(1, n+1):
        current_odd_info = generate_odd_numbers(i, last_odd)
        map.append(current_odd_info[0])
        last_odd = current_odd_info[1]

    return sum(map[-1])


class TestRowSumOddNumbersFunc(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)


if __name__ == '__main__':
    unittest.main()
