from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode

class TestAffineNDecoder(TestCase):
    def test_affine_n_decode(self):
        self.assertEqual(affine_n_decode("XURYWT", 3, 3, 121),"COOLXX")
    def test_affine_n_decode_2(self):
        self.assertEqual(affine_n_decode("USLTFZITNPBJEWREMCQTPQONLCWPJAFFGWWHPZFG", 5, 347, 1721),"THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGXXXX")
    def test_affine_n_decode_lower(self):
        self.assertEqual(affine_n_decode("xurywt",3,3,121),"COOLXX")
    def test_affine_n_decode_3(self):
        self.assertEqual(affine_n_decode("EAPIXBJVUVLAAFFMGWJYQVDLUXIMMLFZMHEUKUUUUUUUU", 15, 15, 1721),
                         "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOGXXXXXXXXX")
