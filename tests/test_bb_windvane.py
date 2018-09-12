import sys
import unittest
from unittest.mock import MagicMock, patch
sys.modules['Adafruit_BBIO'] = MagicMock()
sys.path.append('../')
from windvane.bb_windvane import BBWindvane

class TestBBWindvane(unittest.TestCase):
    def setUp(self):
        # print("Set up for testing")
        self.bb = BBWindvane('NoPin')

    def test_initialize_with_params(self):
        self.assertIsInstance(self.bb, BBWindvane)
        self.assertEqual('NoPin', self.bb.wvPin)

    def test_initialize_without_params(self):
        bb = BBWindvane()
        self.assertIsInstance(bb, BBWindvane)
        self.assertIsNotNone(bb.wvPin)

    def test_set_pin(self):
        pin = 'myPin'
        self.bb.wvPin = pin
        self.assertEqual(self.bb.wvPin, pin)

    def test_get_fixed_resistor_value(self):
        self.assertEqual(10000, self.bb.fixedResistorValue)

    def test_set_fixed_resistor_value(self):
        self.assertEqual(1234, self.bb.set_fixed_resistor_value(1234))

    @patch('windvane.bb_windvane.BBWindvane.read', return_value = 0.5)
    def test_read(self, read):
        self.assertEqual(self.bb.read(), 0.5)

if __name__ == '__main__':
    unittest.main()