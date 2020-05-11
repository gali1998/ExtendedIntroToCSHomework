import unittest
from test_helper import *
from skeleton import *
import random
from hamard import *

class Test_Q4(unittest.TestCase):
    def test_random_subset_sum_count(self):
        L = get_random_list()
        s = random.randrange(0, 101)

        self.assertEqual(subset_sum_count(L, s), count_all_sublists_with_sum(get_all_sublists(L), s))

    def test_random_100_subset_sum_count(self):
        value = True

        for i in range(100):
            L = get_random_list()
            s = random.randrange(0, 101)

            if subset_sum_count(L, s) != count_all_sublists_with_sum(get_all_sublists(L), s):
                value = False
                break
        self.assertTrue(value)

    def test_random_subset_sum_search_all(self):
        L = get_random_list()
        s = random.randrange(0, 101)

        self.assertEqual(len(subset_sum_search_all(L,s)), count_all_sublists_with_sum(get_all_sublists(L), s))

    def test_random_100_subset_sum_search_all(self):
        value = True

        for i in range(100):
            L = get_random_list()
            s = random.randrange(0, 101)

            if len(subset_sum_search_all(L, s)) != count_all_sublists_with_sum(get_all_sublists(L), s):
                value = False
                break

        self.assertTrue(value)

class Test_Q3(unittest.TestCase):
    def test_q3(self):
        value = True

        for i in range(15):
            if had_complete(i) != had(i):
                value = False
                break

        self.assertTrue(value)
