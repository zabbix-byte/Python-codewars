'''
Write a function, which takes a non-negative integer (seconds)
 as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

import unittest
import datetime


def make_readable(seconds):
    secouds = 0
    minutes = 0
    hour = 0

    for _ in range(seconds):
        secouds += 1
        if secouds == 60:
            secouds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

    if secouds < 10:
        secouds = f'0{secouds}'
    if minutes < 10:
        minutes = f'0{minutes}'
    if hour < 10:
        hour = f'0{hour}'

    return f'{hour}:{minutes}:{secouds}'


class TestMakeReadable(unittest.TestCase):
    def test_summations(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(5), "00:00:05")
        self.assertEqual(make_readable(60), "00:01:00")
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")


if __name__ == '__main__':
    unittest.main()
