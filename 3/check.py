from idan import *
from tomer import *
from bar import *
from hw3_207704842 import *

def test_cycle():
    for i in range(2, 500):
        if idan_cycle(i) != cycle(i) or tomer_cycle(i) != cycle(i) or bar_cycle(i) != cycle(i):
            print("problem")
            break

    print("cycle is ok")


def test_complete_graph():
    for i in range(2, 500):
        if idan_complete_graph(i) != complete_graph(i) or tomer_complete_graph(i) != complete_graph(i) or bar_complete_graph(i) != complete_graph(i):
            print("problem")
            break

    print("complete graph is ok")

def test_inv_cycle():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
    for i in primes:
        if idan_inv_cycle(i) != inv_cycle(i) or tomer_inv_cycle(i) != inv_cycle(i) or bar_inv_cycle(i) != inv_cycle(i):
            if (tomer_inv_cycle(i) != inv_cycle(i)):
                print("problem with tomer")
            elif idan_inv_cycle(i) != inv_cycle(i):
                print("problem with idan")
            print("problem" + str(i))
            break

    print("inv cycle is ok")

def test_return_graph():
    for i in range(2, 500):
        if idan_return_graph(i) != return_graph(i) or tomer_return_graph(i) != return_graph(i):
            if(tomer_return_graph(i) != return_graph(i)):
                print("problem with tomer")
            else:
                print("problem with idan")
            print("problem")
            break

    print("return graph is ok")
test_cycle()
test_complete_graph()
test_inv_cycle()
test_return_graph()