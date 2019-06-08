import unittest
from util import get_digit
from util import get_digit_b
from util import get_digit_c


class TestUtil(unittest.TestCase):
    def test_get_digit(self):
        self.assertEqual(get_digit(5438, 1), 8)
        self.assertEqual(get_digit(5438, 2), 3)
        self.assertEqual(get_digit(5438, 3), 4)
        self.assertEqual(get_digit(5438, 4), 5)
        self.assertEqual(get_digit(5438, 5), 0)
        self.assertEqual(get_digit(5438, 20), 0)

    def test_get_digit_b(self):
        self.assertEqual(get_digit_b(5438, 1), 8)
        self.assertEqual(get_digit_b(5438, 2), 3)
        self.assertEqual(get_digit_b(5438, 3), 4)
        self.assertEqual(get_digit_b(5438, 4), 5)
        self.assertEqual(get_digit_b(5438, 5), 0)
        self.assertEqual(get_digit_b(5438, 20), 0)

    def test_get_digit_c(self):
        self.assertEqual(get_digit_c(5438, 1), 8)
        self.assertEqual(get_digit_c(5438, 2), 3)
        self.assertEqual(get_digit_c(5438, 3), 4)
        self.assertEqual(get_digit_c(5438, 4), 5)
