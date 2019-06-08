import unittest
from translator_b import translate


class TestTranslate(unittest.TestCase):
    def test_translate(self):
        roman10 = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
        roman100 = ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C')

        for i, r in enumerate(roman10):  # First 10
            self.assertEqual(translate(i + 1), r)

        for i, r100 in enumerate(roman100):  # From 11 to 111
            for j, r10 in enumerate(roman10):
                self.assertEqual(translate(((i+1)*10 + j+1)), r100 + r10)
