import unittest
from hw6_207704842 import *

class Test_Improved_generator(unittest.TestCase):
    def test_next(self):
        def countup_finite():
            i = 0
            while (i < 4):
                yield i
                i += 1

        improved_g = ImprovedGenerator(countup_finite)

        self.assertFalse(improved_g.has_next())
        self.assertEqual(0, next(improved_g))
        self.assertFalse(improved_g.has_next())
        self.assertEqual(1, next(improved_g))
        self.assertFalse(improved_g.has_next())
        self.assertEqual(2, next(improved_g))
        self.assertTrue(improved_g.has_next())
        self.assertEqual(3, next(improved_g))
        self.assertFalse(improved_g.has_next())



