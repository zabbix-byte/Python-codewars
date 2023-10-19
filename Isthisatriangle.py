'''
Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
'''
import unittest


def is_triangle(a, b, c):
    is_a_triangle = []

    if (a <= 0) or (b <= 0) or (c <= 0):
        return False

    if ((a + b) > c):
        is_a_triangle.append(True)
    if ((a + c) > b):
        is_a_triangle.append(True)
    if ((b + c) > a):
        is_a_triangle.append(True)

    return True if len(is_a_triangle) == 3 else False


class TestIsTriangle(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_triangle(1, 2, 2), True,
                         "didn't work when sides were 1, 2, 2")
        self.assertEqual(is_triangle(7, 2, 2), False,
                         "didn't work when sides were 7, 2, 2")
        self.assertEqual(is_triangle(1, 2, 3), False,
                         "didn't work when sides were 1, 2, 3")
        self.assertEqual(is_triangle(1, 3, 2), False,
                         "didn't work when sides were 1, 3, 2")
        self.assertEqual(is_triangle(3, 1, 2), False,
                         "didn't work when sides were 3, 1, 2")
        self.assertEqual(is_triangle(5, 1, 2), False,
                         "didn't work when sides were 5, 1, 2")
        self.assertEqual(is_triangle(1, 2, 5), False,
                         "didn't work when sides were 1, 2, 5")
        self.assertEqual(is_triangle(2, 5, 1), False,
                         "didn't work when sides were 2, 5, 1")
        self.assertEqual(is_triangle(4, 2, 3), True,
                         "didn't work when sides were 4, 2, 3")
        self.assertEqual(is_triangle(5, 1, 5), True,
                         "didn't work when sides were 5, 1, 5")
        self.assertEqual(is_triangle(2, 2, 2), True,
                         "didn't work when sides were 2, 2, 2")
        self.assertEqual(is_triangle(-1, 2, 3), False,
                         "didn't work when sides were -1, 2, 3")
        self.assertEqual(is_triangle(1, -2, 3), False,
                         "didn't work when sides were 1, -2, 3")
        self.assertEqual(is_triangle(1, 2, -3), False,
                         "didn't work when sides were 1, 2, -3")
        self.assertEqual(is_triangle(0, 2, 3), False,
                         "didn't work when sides were 0, 2, 3")


if __name__ == '__main__':
    unittest.main()
