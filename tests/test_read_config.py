import unittest
from src.read_config import ReadConfig
import os


class TestReadConfig(unittest.TestCase):
    def setUp(self):
        self.directory_path = os.path.dirname(os.path.abspath('__file__'))
        self.rcfg = ReadConfig(self.directory_path + '/config.yaml')

    def test_get_config_keys(self):
        self._keys = ['author', 'contact', 'title', 'social', 'theme'].sort()
        self.assertEqual(self._keys, self.rcfg.get_config_keys().sort())
        
