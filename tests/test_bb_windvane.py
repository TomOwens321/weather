import sys
import unittest
from unittest.mock import MagicMock
sys.modules['Adafruit_BBIO'] = MagicMock()
sys.path.append('../')
from windvane.bb_windvane import BBWindvane

class TestBBWindvane(unittest.TestCase):
    def setUp(self):
        # print("Set up for testing")
        self.bb = BBWindvane()

    def test_initialize_without_params(self):
        self.assertIsInstance(self.bb, BBWindvane)

    def test_initialize_with_params(self):
        bb = BBWindvane(pinno = 'p1.2')
        self.assertIsInstance(bb, BBWindvane)

    def test_read(self):
        self.assertEqual(self.bb.read(), 1.2)

if __name__ == '__main__':
    unittest.main()