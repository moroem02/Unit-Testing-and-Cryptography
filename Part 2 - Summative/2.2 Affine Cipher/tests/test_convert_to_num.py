from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num

class TestConvertToNum(TestCase):
    def test_convert_to_num(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"), 218741750267309021256255930435388550208768849997977)
    def test_convert_to_num_2(self):
        self.assertEqual(convert_to_num("FUNTESTSTRING"),621513975000949529)
    def test_convert_to_num_lowercase(self):
        self.assertEqual(convert_to_num("stringisinlowercase"),138331395742301517548631220)

