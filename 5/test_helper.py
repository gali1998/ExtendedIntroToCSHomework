import itertools
import random
from hw5_207704842 import *
from reference import Binary_search_tree as reference_tree
from reference import Permutation as reference_permutation

def get_permutations(n):
    return list(itertools.permutations([i for i in range(n)]))

def gen_tree_and_rtree(n):
    t = Binary_search_tree()
    tr = reference_tree()
    G = [i for i in range(n)]
    random.shuffle(G)
    for i in G:
        t.insert(i, i)
        tr.insert(i,i)

    return [t, tr]

def are_trees_equal(t1, t2):
    if t1 == None and t2 == None:
        return True
    if (t1 == None and t2 != None) or (t2 == None and t1 != None):
        return False
    if t1.key != t2.key:
        return False
    return are_trees_equal(t1.left, t2.left) and are_trees_equal(t1.right, t2.right)

def get_random_list(n):
    options = [i for i in range(-100, 100)]

    random.shuffle(options)

    return options[:n]
def build_tree_from_list(lst):
    t = Binary_search_tree()

    for item in lst:
        t.insert(item,item)

    return t

def get_values_from_head(doubly_linked):
    result = []

    current = doubly_linked.head

    while current != None:
        result.append(current.value)
        current = current.next
    return result


def get_values_from_tail(doubly_linked):
    result = []

    current = doubly_linked.tail

    while current != None:
        result.append(current.value)
        current = current.prev
    return result
