import unittest
import sys
from src.read_file import File

class TestReadFile(unittest.TestCase):
    def setUp(self):
        self.f = File('2015-10-13-this is a title.md')

    def test_year(self):
        self.assertEqual(self.f.year, '2015')

    def test_month(self):
        self.assertEqual(self.f.month, '10')

    def test_day(self):
        self.assertEqual(self.f.day, '13')

    def test_title(self):
        self.assertEqual(self.f.title, 'this is a title')


class TestIsHiddenFile(unittest.TestCase):
    def setUp(self):
        self.f = File('2015-10-13-this is a title.md~')

    def test_is_hidden_file(self):
        self.assertTrue(self.f.is_hidden_file)
