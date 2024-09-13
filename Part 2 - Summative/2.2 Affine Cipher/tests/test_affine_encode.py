from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode

class TestAffineEncode(TestCase):
    def test_affine_encode(self):
        self.assertEqual(affine_encode("HELLOWORLD",3,9),"EVQQZXZIQS")
    def test_affine_encode_2(self):
        self.assertEqual(affine_encode("THISISANOTHERTEST",9,3),"SOXJXJDQZSONASNJS")
    def test_affine_encode_spaces(self):
        self.assertEqual(affine_encode("HELLO WORLD",3,9),"EVQQZ XZIQS")

    def test_affine_encode_lowercase(self):
        self.assertEqual(affine_encode("helloworld", 3, 9), "EVQQZXZIQS")
    def test_affine_encode_punct(self):
        self.assertEqual(affine_encode("HELLO, WORLD.",3,9), "EVQQZ, XZIQS.")