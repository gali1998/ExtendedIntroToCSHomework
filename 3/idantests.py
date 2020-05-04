from skeleton import *

def print_matrix(matrix):
    for row in matrix:
        print(row)

def test_cycle(prnt=False):
    try:
        cycle(0)
        print("Did not raise cycle 0")
        cycle(1)
        print("Did not raise cycle 1")
    except:
        pass
    if cycle(3) != [[0, 1, 1], [1, 0, 1], [1, 1, 0]]:
        print("Error in cycle 3")
    if cycle(4) != [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]:
        print("Error in cycle 4")
    if prnt:
        for i in range(2, 10):
            print_matrix(cycle(i))

def test_complete(prnt=False):
    for i in range(2,10):
        comp = complete_graph(i)
        s = 0
        for row in comp:
            s += sum(row)
        if s != i**2:
            print("Error for ", i)
            print_matrix(comp)
        if prnt:
            print_matrix(comp)

def test_inv_cycle():
    for n in [2,3,5,7,11]:
        inv_matrix = inv_cycle(n)
        for i in range(1, n):
            inv = (i ** (n - 2)) % n
            if inv_matrix[i][inv] != 1:
                print ("Error for ", n)
            if (i*inv)%n != 1:
                print(i, " ", inv)
                print ((i*inv)%n)
                print ("Error for ", n)
        if inv_matrix[0][0] != 1:
            print("Error for zeros")

def test_return_graph():
    for n in range(2,10):
        g = return_graph(n)
        for i in range (n):
            next_node = (i + 1) % n
            if g[i][next_node] != 1:
                print("Error for next for ", i , ' matrix ', n)
            if i != 0 and g[i][0] != 1:
                print("Error for return for ", i,' matrix ',n)

def test_step():
    for n in range(2,10):
        adj = random_graph(n, 0.9)
        for i in range(n):
            step = random_step(adj,i)
            if adj[i][step] != 1:
                print("Error for ", n, i ,step)

def test_walk():
    for n in range(2,10):
        adj = cycle(n)
        hist = walk_histogram(adj)
        for v in hist:
            if v == 0:
                print("Error for ", n, '. hist: ', hist)

def test_cover_time():
    for n in range(2,10):
        adj = cycle(n)
        hist = walk_histogram(adj)
        time = cover_time(adj)
        if time < n:
            print("Error ", n, " more than ", time)

def test_merge_sorted_blocks():
    x = merge_sorted_blocks([[2,4,6], [1,3,5], [7,8,9], [1,5,19]])
    y = 0

test_cycle()
test_complete()
test_inv_cycle()
test_return_graph()
test_step()
test_walk()
test_cover_time()
test_merge_sorted_blocks()