from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class TestCaesarEncode(TestCase):
    def test_caesar_decode_shift_2(self):
        self.assertEqual(caesar_decode("JGNNQYQTNF", 2),"HELLOWORLD")

    def test_caesar_decode_all_lowercase(self):
        self.assertEqual(caesar_decode("jgnnqyqtnf", 2), "HELLOWORLD")

    def test_caesar_decode_spaces(self):
        self.assertEqual(caesar_decode("mjqqt ctwqi", 5), "HELLO WORLD")

    def test_caesar_decode_punctuation(self):
        self.assertEqual(caesar_decode("mjqqt ctwqi!!!!!!!!", 5), "HELLO WORLD!!!!!!!!")