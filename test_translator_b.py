import unittest
import translator_a
import translator_b


class TestTranslate(unittest.TestCase):
    def test_translate_to_roman_b(self):
        for decimal in range(1, 4000):
            self.assertEqual(translator_a.translate(decimal), translator_b.translate_to_roman(decimal))

    def test_translate_to_decimal_b(self):
        for decimal in range(1, 4000):
            roman = translator_a.translate(decimal)
            self.assertEqual(decimal, translator_b.translate_to_decimal(roman))
