import unittest # this allows you to use assert fuctions
from skeleton import * # this allows me to use functions i wrote in the skeleton file

# we put the tests of each function in a class
class TestFunction(unittest.TestCase):
    # here i will test some base cases
    def TestBaseCases(self):
        self.assertTrue(sub(6,2) == 4)
        self.assertEqual(sub(6,2), 4)
        self.assertNotEqual(sub(6,2), 6)