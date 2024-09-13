from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_decode

class TestAffineDecode(TestCase):
    def test_affine_decode(self):
        self.assertEqual(affine_decode("EVQQZXZIQS",3,9), "HELLOWORLD")
    def test_affine_encode_2(self):
        self.assertEqual(affine_decode("SOXJXJDQZSONASNJS",9,3),"THISISANOTHERTEST")
    def test_affine_encode_spaces(self):
        self.assertEqual(affine_decode("EVQQZ XZIQS",3,9),"HELLO WORLD")

    def test_affine_encode_lowercase(self):
        self.assertEqual(affine_decode("evqqzxziqs", 3, 9), "HELLOWORLD")
    def test_affine_encode_punct(self):
        self.assertEqual(affine_decode("EVQQZ, XZIQS.",3,9), "HELLO, WORLD.")