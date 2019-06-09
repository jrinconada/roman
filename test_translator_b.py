import unittest
import translator_a
import translator_b


class TestTranslate(unittest.TestCase):
    def test_translate_b(self):
        for i in range(1, 4000):
            self.assertEqual(translator_a.translate(i), translator_b.translate_to_roman(i))
