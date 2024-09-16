from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import affine_n_encode

class TestAffineNEncode(TestCase):
    def test_affine_n_encode(self):
        self.assertEqual(affine_n_encode("COOL", 3, 3, 121),"XURYWT")
    def test_affine_n_encode_2(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", 5, 347, 1721),"USLTFZITNPBJEWREMCQTPQONLCWPJAFFGWWHPZFG")
    def test_affine_n_encode_lowercase(self):
        self.assertEqual(affine_n_encode("cool", 3, 3, 121),"XURYWT")
    def test_affine_n_encode_3(self):
        self.assertEqual(affine_n_encode("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG", 15, 15, 1721),"EAPIXBJVUVLAAFFMGWJYQVDLUXIMMLFZMHEUKUUUUUUUU")