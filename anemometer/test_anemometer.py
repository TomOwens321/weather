from anemometer import Anemometer
import unittest

class TestAnemometer(unittest.TestCase):
    def test_instantiate(self):
        anem = Anemometer()
        self.assertIsInstance(anem, Anemometer)

def run_tests():
    unittest.main()

if __name__ == '__main__':
    run_tests()
