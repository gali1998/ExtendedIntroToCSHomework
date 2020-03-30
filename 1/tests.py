import random
import unittest
from hw1_207704842 import *
from primes_lst import *

class TestHW1(unittest.TestCase):
    def test_random_q6(self):
        num = random.randrange(4, 100000, 2)
        result = check_goldbach_for_range(num, primes)
        self.assertEqual(result, True)

    def test100(self):
        for i in range(100):
            num = random.randrange(4, 10000, 2)
            result = check_goldbach_for_range(num, primes)

            if result == False:
                break
        self.assertEqual(result, True)

    def testremove2(self):
        lst = primes.copy()
        lst.remove(2)

        result = check_goldbach_for_range(6, lst)
        self.assertEqual(result, False)

    def testremove3(self):
        lst = primes.copy()
        lst.remove(3)

        self.assertEqual(check_goldbach_for_range(8, lst), False)

    def testremove5(self):
        lst1 = primes.copy()
        lst1.remove(5)

        self.assertEqual(check_goldbach_for_range(6, lst1), True)
