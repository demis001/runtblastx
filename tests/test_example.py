import unittest
from python_template import python_template

class Test(unittest.TestCase):
    def test_returns_true(self):
        self.assertEquals(True, python_template.returns_true())
        self.assertTrue(python_template.returns_true())

    def test_will_pass(self): 
        self.assertTrue(True)   
