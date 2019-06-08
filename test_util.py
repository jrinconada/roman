import unittest
from util import get_digit


class TestGetDigit(unittest.TestCase):
    def test_get_digit(self):
        self.assertEqual(get_digit(5438, 1), 8)
        self.assertEqual(get_digit(5438, 2), 3)
        self.assertEqual(get_digit(5438, 3), 4)
        self.assertEqual(get_digit(5438, 4), 5)
