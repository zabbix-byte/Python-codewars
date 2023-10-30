import unittest


def reverse_words(s):
    return ' '.join([i for i in s.split(' ')][::-1])


class TestReverse(unittest.TestCase):
    def test_dig_pow(self):
        self.assertEqual(reverse_words("hello world!"), "world! hello")


if __name__ == '__main__':
    unittest.main()
