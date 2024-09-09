from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode

class TestSubEncode(TestCase):
    def test_sub_encode(self):
        self.assertEqual(sub_encode("THISISATEST","FSQWCNRVEAJTIXYOLZGKHBDMPU"),"KVEGEGFKCGK")

    def test_sub_encode_lowercase(self):
        self.assertEqual(sub_encode("thisisatest", "FSQWCNRVEAJTIXYOLZGKHBDMPU"), "KVEGEGFKCGK")
    def test_sub_encode_spaces(self):
        self.assertEqual(sub_encode("this is a test", "FSQWCNRVEAJTIXYOLZGKHBDMPU"), "KVEG EG F KCGK")
    def test_sub_encode_punctuation(self):
        self.assertEqual(sub_encode("hello, world. this is a test!", "QDOIPFUYRTJBXMSLZAGHECWVKN"), "YPBBS, WSABI. HYRG RG Q HPGH!")
    def test_sub_encode_no_faulty_cipher(self):
        self.assertEqual(sub_encode("hello world!", "QDOIPFUYN"), "YPCCH VHLCI!")
