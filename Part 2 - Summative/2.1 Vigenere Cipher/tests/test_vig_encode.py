from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class TestVigEncode(TestCase):
    def test_vig_encode(self):
        self.assertEqual(vig_encode("THISISATESTMESSAGE","THEKEY"),"LOMBMPT IBXJXZWKKB")
    def test_vig_encode_spaces(self):
        self.assertEqual(vig_encode("THIS IS A TEST","NEWKEY"),"FLDBDFEDWJXBEX")
    def test_vig_encode_lowercase(self):
        self.assertEqual(vig_encode("thisisatest","NEWKEY"),"FLDBMPNX BX")
    def test_vig_encode_punctuation(self):
        self.assertEqual(vig_encode("Hello, world! This is a test.","PUNCTUATION"),"WYYNG,TWGZZQ!OMUKKTIKHOMHYEV.")
    def test_vig_encode_key_with_spaces(self):
        self.assertEqual(vig_encode("TESTMESSAGETOBEENCODED", "FUN KEY"),"YYESWIPXUTDCSZJY BYHBI")
