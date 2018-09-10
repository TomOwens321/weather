import unittest
import sys
sys.path.append('../')
from windvane.windvane import Windvane

class TestWindvane(unittest.TestCase):
    def setUp(self):
        self.wind = Windvane()

    def test_instantiate(self):
        self.assertIsInstance(self.wind, Windvane)

    def test_direction_text(self):
        self.assertEqual("ESE", self.wind.direction_text(0.01))
        self.assertEqual("ESE", self.wind.direction_text(0.23))
        self.assertEqual("ENE", self.wind.direction_text(0.24))
        self.assertEqual("ENE", self.wind.direction_text(0.27))
        self.assertEqual("E  ", self.wind.direction_text(0.28))
        self.assertEqual("E  ", self.wind.direction_text(0.34))

    def test_direction_returns_reading_on_not_found(self):
        value = 100
        self.assertEqual(str(value * 100), self.wind.direction_text(value))

    def tearDown(self):
        self.wind = None

def run_tests():
    unittest.main()

if __name__ == '__main__':
    run_tests()
