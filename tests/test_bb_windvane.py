import sys
import unittest
from unittest.mock import MagicMock
sys.modules['Adafruit_BBIO'] = MagicMock()
sys.path.append('../')
from windvane.bb_windvane import BBWindvane

class TestBBWindvane(unittest.TestCase):
    def setUp(self):
        # print("Set up for testing")
        self.bb = BBWindvane('NoPin')

    def test_initialize_with_params(self):
        self.assertIsInstance(self.bb, BBWindvane)
        self.assertEqual('NoPin', self.bb.anemometerPin)

    def test_initialize_without_params(self):
        bb = BBWindvane()
        self.assertIsInstance(bb, BBWindvane)
        self.assertIsNotNone(bb.anemometerPin)

    def test_read(self):
        self.assertEqual(self.bb.read(), 1.2)

    def test_get_fixed_resistor_value(self):
        self.assertEqual(10000, self.bb.fixedResistorValue)

    def test_set_fixed_resistor_value(self):
        self.assertEqual(1234, self.bb.set_fixed_resistor_value(1234))

if __name__ == '__main__':
    unittest.main()