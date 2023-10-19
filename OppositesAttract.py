'''
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
'''
import unittest


def even(number: int) -> bool:
    return number % 2 == 0


def lovefunc(flower1, flower2):
    one_is_odd = False
    flower1_is_odd = even(flower1)
    flower2_is_odd = even(flower2)

    if (flower1_is_odd or flower2_is_odd):
        one_is_odd = True

    if ((flower1_is_odd is False) or (flower2_is_odd is False)) and one_is_odd:
        return True

    return False


class TestLoveFunc(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(lovefunc(1, 4), True)
        self.assertEqual(lovefunc(2, 2), False)
        self.assertEqual(lovefunc(0, 1), True)
        self.assertEqual(lovefunc(0, 0), False)


if __name__ == '__main__':
    unittest.main()
