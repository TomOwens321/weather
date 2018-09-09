import unittest
import sys
sys.path.append('../')
from weather.anemometer import Anemometer

class TestAnemometer(unittest.TestCase):
    def test_instantiate(self):
        anem = Anemometer(2)
        self.assertIsInstance(anem, Anemometer)

if __name__ == '__main__':
    unittest.main()