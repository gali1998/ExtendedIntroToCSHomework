from hw5_207704842 import *
from reference import *
import random
from test_helper import *
from reference import Permutation as referenece_Permutation
import time

def generate_long_string():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x', 'y','z']

    str = ""
    for i in range(2000):
        str += random.choice(letters)

    return "A"*2000

def get_random_list():
    n = random.randrange(5, 20)
    lst = []

    for i in range(n):
        lst.append(generate_long_string())

    return lst

def compare_runitmes():
    k = random.randrange(1, 2000)
    lst = get_random_list()

    t1 = time.perf_counter()
    prefix_suffix_overlap(lst, k)
    t2 = time.perf_counter()

    t3 = time.perf_counter()
    prefix_suffix_overlap_hash1(lst, k)
    t4 = time.perf_counter()

    t5 = time.perf_counter()
    prefix_suffix_overlap_hash2(lst, k)
    t6 = time.perf_counter()

    print("no hash: "+ str(t2-t1))
    print("hash1: " + str(t4 - t3))
    print("hash2: " + str(t6 - t5))

for i in range(10):
    print("===========================")
    compare_runitmes()
    print("===========================")
