import unittest
from util import get_digit
import translator_a
import translator_b


class TestTranslate(unittest.TestCase):
    def test_translate_b(self):
        for i in range(1, 4000):
            self.assertEqual(translator_a.translate(i), translator_b.translate(i))
