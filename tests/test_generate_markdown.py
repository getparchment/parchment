import unittest
from src.generate import GenerateMarkdown

class TestGenerateMarkdown(unittest.TestCase):
    def setUp(self):
        self.gm = GenerateMarkdown('I am using **mistune markdown parser**')
        
    def test_generate_markdown(self):
        self.assertEqual(self.gm.output, '<p>I am using <strong>mistune markdown parser</strong></p>\n')
