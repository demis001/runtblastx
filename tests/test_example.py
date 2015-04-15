import unittest
from runtblastx import runtblastx

class Test(unittest.TestCase):
    def test_returns_true(self):
        self.assertEquals(True, runtblastx.returns_true())
        self.assertTrue(runtblastx.returns_true())

    def test_will_pass(self): 
        self.assertTrue(True)   
