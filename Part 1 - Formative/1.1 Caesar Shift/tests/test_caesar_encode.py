from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestCaesarEncode(TestCase):
    def test_caesar_encode_shift_2(self):
        self.assertEqual(caesar_encode("HELLOWORLD", 2),"JGNNQYQTNF")

    def test_caesar_encode_all_lowercase(self):
        self.assertEqual(caesar_encode("helloworld", 2), "JGNNQYQTNF")

    def test_caesar_encode_spaces(self):
        self.assertEqual(caesar_encode("hello world", 5), "MJQQT CTWQI")

    def test_caesar_encode_punctuation(self):
        self.assertEqual(caesar_encode("hello world!!!!!!!!", 5), "MJQQT CTWQI!!!!!!!!")