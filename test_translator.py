import unittest
from translator import translate


class TestTranslate(unittest.TestCase):
    def test_translate(self):
        roman = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
        for i, r in enumerate(roman):
            self.assertEqual(translate(i + 1), r)
