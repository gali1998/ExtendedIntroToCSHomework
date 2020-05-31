import unittest
import random
from test_helper import *
from hw5_207704842 import *
from reference import Binary_search_tree as reference_tree
from reference import Permutation as reference_permutation

class Test_q4(unittest.TestCase):
    def test_delete(self):
        l = [i for i in range(100)]
        lst = DLList(l)

        lst.delete_node(lst.head)
        lst.delete_node(lst.tail)
        c = lst.head

        for i in range(10):
            c = c.next

        deleted_value = c.value
        lst.delete_node(c)

        head = get_values_from_head(lst)
        tail = get_values_from_tail(lst)
        tail.reverse()
        self.assertEqual(head, tail)
        self.assertEqual(lst.len, len(l) - 3)
        self.assertFalse(0 in head)
        self.assertFalse(99 in head)
        self.assertFalse(deleted_value in head)
    def test_rotate(self):
        result = True
        n = random.randrange(2, 10)
        l = get_random_list(n)
        k = random.randrange(1, n)
        lst = DLList(l)
        lst.rotate(k)
        head = get_values_from_head(lst)
        tail = get_values_from_tail(lst)
        tail.reverse()
        self.assertEqual(head, tail)
        for i in range(n):
            if l[i] != tail[(i + k)  % n]:
                result = False
                break
        self.assertTrue(result)
    def test_reverse(self):
        l = get_random_list(30)
        lst = DLList(l)
        lst.reverse()

        self.assertEqual(get_values_from_tail(lst), l)
        l.reverse()

        self.assertEqual(get_values_from_head(lst), l)
    def test_insert(self):
        lst = DLList(get_random_list(10))
        head = get_values_from_head(lst)
        tail = get_values_from_tail(lst)
        tail.reverse()

        self.assertEqual(head, tail)

        lst.insert("a")
        self.assertEqual(lst.tail.value, "a")
        head = get_values_from_head(lst)
        tail = get_values_from_tail(lst)
        tail.reverse()

        self.assertEqual(head, tail)

        lst.insert("b", True)
        self.assertEqual(lst.tail.value, "a")
        self.assertEqual(lst.head.value, "b")
        head = get_values_from_head(lst)
        tail = get_values_from_tail(lst)
        tail.reverse()

        self.assertEqual(head, tail)

class Test_q3(unittest.TestCase):
    def test_random(self):
        n = random.randrange(1, 50)

        l1 = get_random_list(n)
        l2 = get_random_list(n)

        self.assertEqual(same_tree(l1, l2), are_trees_equal(build_tree_from_list(l1).root, build_tree_from_list(l2).root))
    def test_random100(self):
        result = True
        for i in range(100):
            n = random.randrange(0, 50)

            l1 = get_random_list(n)
            l2 = get_random_list(n)

            if same_tree(l1, l2) != are_trees_equal(build_tree_from_list(l1).root, build_tree_from_list(l2).root):
                result = False
                break

        self.assertTrue(result)
class Test_q2(unittest.TestCase):
    def test_max_sum(self):
        n = random.randrange(1,100)
        trees = gen_tree_and_rtree(n)

        t = trees[0]
        tr = trees[1]

        self.assertEqual(t.max_sum(), tr.max_sum())

    def test_max_sum_100(self):
        result = True
        for i in range(100):
            n = random.randrange(1, 100)
            trees = gen_tree_and_rtree(n)

            t = trees[0]
            tr = trees[1]

            if t.max_sum() != tr.max_sum():
                result = False
                break
        self.assertTrue(result)

    def test_is_balanced(self):
        n = random.randrange(1, 100)
        trees = gen_tree_and_rtree(n)


        t = trees[0]
        tr = trees[1]

        self.assertEqual(t.is_balanced(), tr.is_balanced())

    def test_is_balanced_100(self):
        result = True
        for i in range(1000000):
            n = random.randrange(1, 5)
            trees = gen_tree_and_rtree(n)

            t = trees[0]
            tr = trees[1]

            if t.is_balanced() != tr.is_balanced():
                result = False
                break
        self.assertTrue(result)
    def test_diam(self):
        n = random.randrange(1, 100)
        trees = gen_tree_and_rtree(n)


        t = trees[0]
        tr = trees[1]

        self.assertEqual(t.diam(), tr.diam())

    def test_diam_100(self):
        result = True
        for i in range(10000):
            n = random.randrange(1, 100)
            trees = gen_tree_and_rtree(n)

            t = trees[0]
            tr = trees[1]

            if t.diam() != tr.diam():
                result = False
                break
        self.assertTrue(result)

class TestPermutation(unittest.TestCase):
    def test_random_permutation_init(self):
        result = True
        n = random.randrange(10)
        permutations = get_permutations(n)

        for perm in permutations:
            p = Permutation(perm)

            if p.perm == None:
                result = False
                break

        self.assertTrue(result)

    def test_not_permutation_init(self):
        self.assertIsNone(Permutation([1,2]).perm)
        self.assertIsNone(Permutation([0, 0]).perm)
        self.assertIsNone(Permutation([-1, 0]).perm)

    def test_compose(self):
        n = random.randrange(10)
        permutations = get_permutations(n)
        perm1 = Permutation(random.choice(permutations))
        perm2 = Permutation(random.choice(permutations))
        composed = perm1.compose(perm2)

        is_composition = True

        for i in range(n):
            if composed[i] != perm1[perm2[i]]:
                is_composition = False
        self.assertTrue(is_composition)


    def test_compose_and_inv(self):
        result = True
        n = random.randrange(10)
        permutations = get_permutations(n)
        id_perm = Permutation([i for i in range(n)])

        for perm in permutations:
            p = Permutation(perm)
            inv = p.inv()

            if p.compose(inv) != id_perm:
                result = False
                break

        self.assertTrue(result)

    def test_compose_list(self):
        n = random.randrange(2,10)
        permutations = get_permutations(n)
        lst_options = []
        for i in range(len(permutations)):
            lst_options.append(Permutation(permutations[i]))
        if len(lst_options) == 0:
            k = 0
        else:
            k = random.randrange(1, 20)
        lst = []

        for i in range(k):
            lst.append(random.choice(lst_options))

        composed = compose_list(lst)

        resl_composed = lst[0]

        for i in range(1, k):
            resl_composed = resl_composed.compose(lst[i])

        self.assertEqual(resl_composed, composed)

    def test_order(self):
        n = random.randrange(10)
        permutations = get_permutations(n)
        identity = Permutation([i for i in range(n)])
        perm = identity.perm
        while perm == identity.perm:
            perm = random.choice(permutations)
        p = Permutation(perm)

        lst = []
        k = p.order()

        for i in range(k):
            lst.append(p)

        before_k = compose_list(lst[1:])
        with_k = compose_list(lst)
        print(before_k.perm)

        self.assertEqual(identity.order(), 1)
        self.assertEqual(identity, with_k)
        self.assertNotEqual(identity, before_k)


