'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''

import unittest


def find_short(s):
    return len(sorted(s.split(' '), key=len)[0])


class TestFindShortFunc(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(find_short(
            "bitcoin take over the world maybe who knows perhaps"), 3)
        self.assertEqual(find_short(
            "turns out random test cases are easier than writing out basic ones"), 3)
        self.assertEqual(find_short(
            "lets talk about javascript the best language"), 3)
        self.assertEqual(find_short(
            "i want to travel the world writing code one day"), 1)
        self.assertEqual(find_short(
            "Lets all go on holiday somewhere very cold"), 2)
        self.assertEqual(find_short("Let's travel abroad shall we"), 2)


if __name__ == '__main__':
    unittest.main()
