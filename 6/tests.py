import unittest
from hw6_207704842 import *
from testhelper import *

class Test_Is_Rotated(unittest.TestCase):
    def test_is_rotated(self):
        s = randomString()
        n = random.randrange(0, len(s))
        t1 = (rotate(s, 1))
        t2 = get_string_with_one_different_char(s)
        t3 = t1+"a"
        print(s)
        print(t1)

        self.assertTrue(is_rotated_1(s, t1))
        self.assertTrue(is_rotated_2(s, t1))
        self.assertFalse(is_rotated_1(s, t2))
        self.assertFalse(is_rotated_2(s, t2))
        self.assertFalse(is_rotated_2(s, t3))
    def test_x(self):
        print(is_rotated_2("zdwtffnohb", "dwtffnohbz"))
        self.assertTrue(is_rotated_2("zdwtffnohb", "dwtffnohbz"))

    def test_100(self):
        result = True
        for i in range(10):
            s = randomString()
            n = random.randrange(0, len(s))
            t2 = get_string_with_one_different_char(s)

            for i in range(0,n):
                t1 = (rotate(s, i))
                print(s)
                print(t1)
                self.assertTrue(is_rotated_1(s, t1))
                self.assertTrue(is_rotated_2(s, t1))
                self.assertFalse(is_rotated_1(s, t2))
                self.assertFalse(is_rotated_2(s, t2))
        self.assertTrue(result)
class Test_Improved_generator(unittest.TestCase):
    def test_next(self):
        def countup_finite():
            i = 0
            while (i < 4):
                yield i
                i += 1

        improved_g = ImprovedGenerator(countup_finite())

        self.assertTrue(improved_g.has_next())
        self.assertEqual(0, improved_g.peek())
        self.assertEqual(0, next(improved_g))
        self.assertTrue(improved_g.has_next())
        self.assertEqual(1, improved_g.peek())
        self.assertEqual(1, next(improved_g))
        self.assertTrue(improved_g.has_next())
        self.assertEqual(2, improved_g.peek())
        self.assertEqual(2, next(improved_g))
        self.assertTrue(improved_g.has_next())
        self.assertEqual(3, improved_g.peek())
        self.assertEqual(3, next(improved_g))
        self.assertEqual(None, improved_g.peek())
        self.assertFalse(improved_g.has_next())

        self.assertRaises(StopIteration, next, improved_g)
        self.assertFalse(improved_g.has_next())

    def test_product(self):
        g1 = (i for i in range(10))
        g2 = (i for i in range(10, 20))
        improved_g1 = ImprovedGenerator(g1)
        improved_g2 = ImprovedGenerator(g2)
        g = improved_g1.product(improved_g2)

        for i in range(10):
            n = i
            print(n)
            self.assertTrue(g.has_next())
            print(g.peek())
            self.assertEqual((n, n+10), g.peek())
            self.assertEqual((n, n + 10), next(g))

        self.assertFalse(g.has_next())

        self.assertRaises(StopIteration, next, g)
        self.assertFalse(g.has_next())


