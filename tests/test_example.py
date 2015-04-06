import unittest
import python_template

class Test(unittest.TestCase):

    def test_returns_true(self):
        self.assertEquals(True, example.returns_true())
        self.assertTrue(example.returns_true())

    def test_will_pass(self): 
        self.assertTrue(True)   
