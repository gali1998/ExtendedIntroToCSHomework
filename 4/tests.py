import unittest
from test_helper import *
from hw4_207704842 import *
import random
from hamard import *

class Test_Q2(unittest.TestCase):
    def test_q2(self):
        value = True

        for i in range(1,10):
            for j in range(1,10):
                result1 = win(i, j)
                result2 = win_fast(i, j)

                if i == j and (result1 == True or result2 == True):
                    value = False
                    break

                if i != j and (result1 != True or result2 != True):
                    value = False
                    break

        self.assertTrue(value)

class Test_Q4(unittest.TestCase):
    def test_random_subset_sum_count(self):
        L = get_random_list()
        s = random.randrange(-101, 101)

        self.assertEqual(subset_sum_count(L, s), count_all_sublists_with_sum(get_all_sublists(L), s))

    def test_random_100_subset_sum_count(self):
        value = True

        for i in range(10000  ):
            L = get_random_list()
            s = random.randrange(-101, 101)

            if subset_sum_count(L, s) != count_all_sublists_with_sum(get_all_sublists(L), s):
                value = False
                break
        self.assertTrue(value)

    def test_random_subset_sum_search_all(self):
        L = get_random_list()
        s = random.randrange(-101, 101)

        self.assertEqual(len(subset_sum_search_all(L,s)), count_all_sublists_with_sum(get_all_sublists(L), s))

    def test_random_100_subset_sum_search_all(self):
        value = True

        for i in range(10000):
            L = get_random_list()
            s = random.randrange(-101, 101)

            if len(subset_sum_search_all(L, s)) != count_all_sublists_with_sum(get_all_sublists(L), s):
                value = False
                break

        self.assertTrue(value)

class Test_Q3(unittest.TestCase):
    def test_q3(self):
        value = True

        for i in range(10):
            if had_complete(i) != had(i):
                value = False
                break

        self.assertTrue(value)

class Test_Q6(unittest.TestCase):
    def test_random_q6(self):
        s1 = get_random_string()
        s2 = get_random_string()

        self.assertEqual(levenshtein(s1, s2), distance(s1,s2))
        self.assertEqual(levenshtein(s1, s2), distance_fast(s1,s2))

    def test_random_100_q6(self):
        value = True

        for i in range(100):
            s1 = get_random_string()
            s2 = get_random_string()

            if levenshtein(s1, s2) != distance_fast(s1,s2) or levenshtein(s1, s2) != distance(s1,s2):
                value = False
                break
        self.assertTrue(value)
