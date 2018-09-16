#!/usr/bin/env python3
import sys
import unittest
from unittest.mock import MagicMock, patch
sys.modules['paho'] = MagicMock()
sys.modules['paho.mqtt'] = MagicMock()
sys.modules['paho.mqtt.client'] = MagicMock()
sys.modules['pyownet'] = MagicMock()
sys.path.append('../')
from pytemps import pytemps

class TestPytemps(unittest.TestCase):
    def setUp(self):
        pass

    @patch('pytemps.pytemps.mqtt_publish')
    def test_log_message(self, mqtt_publish):
        pytemps.log_message('Message')
        pytemps.mqtt_publish.assert_called_once_with(unittest.mock.ANY, unittest.mock.ANY)

    def test_the_truth(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()