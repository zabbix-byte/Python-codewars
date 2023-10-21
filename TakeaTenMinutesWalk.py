'''
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment,
so you decided to take the opportunity to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones
-- everytime you press the button it sends you an array of one-letter 
strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block for each letter (direction)
and you know it takes you one minute to traverse one city block,
so create a function that will return true if the walk the app gives you will
take you exactly ten minutes (you don't want to be early or late!) and will,
 of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment 
of direction letters ('n', 's', 'e', or 'w' only).
It will never give you an empty array (that's not a walk, that's standing still!).
'''

import unittest


def is_valid_walk(walk):
    pos_x, pos_y = 0, 0

    if len(walk) != 10:
        return False

    for i in walk:
        if i == 'n':
            pos_x += 1
        elif i == 's':
            pos_x -= 1
        elif i == 'w':
            pos_y += 1
        elif i == 'e':
            pos_y -= 1

    if pos_x == 0 and pos_y == 0:
        return True

    return False


class TestBasicOpFunc(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_valid_walk(
            ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), True, 'should return True')

    def test_2(self):
        self.assertEqual(is_valid_walk(
            ['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']), False, 'should return False')

    def test_3(self):
        self.assertEqual(is_valid_walk(['w']), False, 'should return False')

    def test_4(self):
        self.assertEqual(is_valid_walk(
            ['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']), False, 'should return False')


if __name__ == '__main__':
    unittest.main()
