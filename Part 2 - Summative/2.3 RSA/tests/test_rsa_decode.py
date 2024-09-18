from unittest import TestCase

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import rsa_decode

class testRSADecodeTestCase(TestCase):
    def test_rsa_decode(self):
        m = 292361466231755597564095925310764764819 * 307125506157764866722739041634199200019
        self.assertEqual(rsa_decode(34028226424022141662679340496616735128390579906964150145035108807466384852365,
                                    m,21266554735539990938794214424150057032684401233730383604860243814738045553417,
                                    len("THEFIVEBOXINGWIZARDSJUMPQUICKLY")), "THEFIVEBOXINGWIZARDSJUMPQUICKLY")
    def test_rsa_decode_2(self):
        self.assertEqual(rsa_decode(69668958482447747683147366014690696767998843751332153785771,
                                    1403667074891238112782266716321710919652719338355971758182859,
                                    439089044392408449427792696511326034882750581330426013280353,
                                    13),"FUNNEWMESSAGE")
    def test_rsa_decode_2(self):
        self.assertEqual(rsa_decode(467748569872613183067748873822174490706742228771828702195430,
                                    1400646771743114725754206640320332528437451377459467742613577,
                                    10771411156423544284604424168336273207821284902303108628865,
                                    13),"FUNNEWMESSAGE")