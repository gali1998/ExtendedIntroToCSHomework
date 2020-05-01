import unittest
from skeleton import *
from testhelper import *

class TestQ3(unittest.TestCase):
    def test_random_100(self):
        result = True

        for i in range(6000000):
            lst = create_random_list()
            copy = lst.copy()
            copy.sort()
            if len(lst) != 1:
                k = random.randrange(1, len(lst))
            else:
                k = 1

            if sort_by_block_merge(lst, k) != copy:
                result = False
                break

        self.assertTrue(result)

    def test_random(self):
        lst = create_random_list()
        copy = lst.copy()
        copy.sort()
        if len(lst) != 1:
            k = random.randrange(1, len(lst))
        else:
            k = 1
        self.assertEqual(sort_by_block_merge(lst, k), copy)

class TestQ4(unittest.TestCase):
    def test_find2_100(self):
        result = True
        for i in range(6000000):
            lst = creaste_rotated_random_list_not_unique()

            s = random.choice(lst)
            result = find2(lst, s)

            if find2(lst, s) == None or s != lst[result]:
                result = False

        self.assertTrue(result)

    def test_find2(self):
        lst = creaste_rotated_random_list_not_unique()

        s = random.choice(lst)

        self.assertEqual(s, lst[find2(lst, s)])
        self.assertEqual(None, find2(lst, -200))

    def test_find_random100(self):
        result= True

        for i in range(6000000):
            lst = get_random_rotated_list()

            s = random.choice(lst)

            if find(lst, s) == None or s != lst[find(lst, s)]:
                print(lst)
                print(s)
                print(find(lst, s))
                result = False
                break

        self.assertTrue(result)

    def test_find_random(self):
        lst = get_random_rotated_list()

        s = random.choice(lst)

        self.assertEqual(s, lst[find(lst, s)])

    def test_find_missing_random(self):
        n = random.randrange(1, 10000)
        k = random.randrange(0, n)

        lst = [i for i in range(0, n) if i != k]

        self.assertEqual(find_missing(lst, k), k)

    def test_find_missing_random100(self):
        result = True

        for i in range(100):
            n = random.randrange(1, 10000)
            k = random.randrange(0, n)

            lst = [i for i in range(0, n) if i != k]

            if find_missing(lst, k) != k:
                result = False

                break

        self.assertTrue(result)

class TestQ5(unittest.TestCase):
    def test_sort(self):
        n = random.randrange(1, 30)
        k = random.randrange(1, 10)

        lst = [get_random_string(k) for i in range(n)]
        lst1 = lst.copy()
        lst2 = lst.copy()
        lst3 = lst.copy()
        lst1.sort()

        self.assertEqual(sort_strings1(lst2, k), lst1)
        self.assertEqual(sort_strings2(lst3, k), lst1)

    def test_int_to_string_random(self):
        k = random.randrange(1, 30)
        n = random.randrange(0, 5**k)

        self.assertEqual(string_to_int(int_to_string(k, n)), n)

    def test_int_to_string_for_all_values(self):
        k = random.randrange(1, 10)

        result = True

        for i in range(0, 5**k):
            if string_to_int(int_to_string(k, i)) != i:
                result = False
                break

        self.assertTrue(result)

    def test_string_to_int_random(self):
        k = random.randrange(1, 30)
        str1 = get_random_string(k)
        str2 = get_random_string(k)

        self.assertEqual(string_to_int(str1) >= string_to_int(str2), str1 >= str2)

    def test_string_to_int_random100(self):
        result = True

        for i in range(100):
            k = random.randrange(1, 30)
            str1 = get_random_string(k)
            str2 = get_random_string(k)
            val1 = string_to_int(str1)>= string_to_int(str2)
            val2 = str1 >= str2

            if  val1 != val2:
                print(str1+ " " + str2)
                result = False

                break
        self.assertTrue(result)
