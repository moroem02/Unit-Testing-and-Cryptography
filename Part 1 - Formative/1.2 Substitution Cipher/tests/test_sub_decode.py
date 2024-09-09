from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode

class TestSubDecode(TestCase):
    def test_sub_decode(self):
        self.assertEqual(sub_decode("KVEGEGFKCGK","FSQWCNRVEAJTIXYOLZGKHBDMPU"),"THISISATEST")

    def test_sub_decode_lowercase(self):
        self.assertEqual(sub_decode("kveg eg f kcgk", "FSQWCNRVEAJTIXYOLZGKHBDMPU"), "THIS IS A TEST")
    def test_sub_decode_spaces(self):
        self.assertEqual(sub_decode("kveg eg f kcgk", "FSQWCNRVEAJTIXYOLZGKHBDMPU"), "THIS IS A TEST")
    def test_sub_decode_punctuation(self):
        self.assertEqual(sub_decode("ypbbs, wsabi. hyrg rg q hpgh!", "QDOIPFUYRTJBXMSLZAGHECWVKN"), "HELLO, WORLD. THIS IS A TEST!")
    def test_sub_decode_no_faulty_cipher(self):
        self.assertEqual(sub_decode("ypcch vhlci!", "QDOIPFUYN"), "HELLO WORLD!")
