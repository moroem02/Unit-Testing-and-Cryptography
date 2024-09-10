from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class TestVigDecode(TestCase):
    def test_vig_decode(self):
        self.assertEqual(vig_decode("FLDBDFEDWJXBEX","NEWKEY"),"THIS IS A TEST")
    def test_vig_decode_spaces(self):
        self.assertEqual(vig_decode("LOMBMPT IBXJXZWKKB","THEKEY"),"THISISATESTMESSAGE")
    def test_vig_decode_lowercase(self):
        self.assertEqual(vig_decode("fldbmpnx bx","NEWKEY"),"THISISATEST")
    def test_vig_decode_punctuation(self):
        self.assertEqual(vig_decode("Wyyng,twgzzq!OMUKKTIKHOMHYEV.","PUNCTUATION"),"HELLO, WORLD! THIS IS A TEST.")
    def test_vig_decode_key_with_spaces(self):
        self.assertEqual(vig_decode("YYESWIPXUTDCSZJXRBYHBI", "FUN KEY"),"TESTMESSAGETOBEDECODED")
