# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).


import random


############
# QUESTION 2
############

def isInCycle(i, j, n):
    return (i - j == 1 or i - j == -1 or (i == n-1 and j == 0) or (j == n-1 and i == 0))

def cycle(n):
    return [[1 if isInCycle(i, j, n) else 0 for j in range(n)] for i in range(n)]


def complete_graph(n):
    return [[1] * n ] * n


def random_graph(n, p):
    return [[1 if random.random() <= p else 0 for j in range(n)] for i in range(n)]

def inv_cycle(n):
    return [[1 if isInCycle(i, j, n) or j * i == 1 % n else 0 for j in range(n)] for i in range(n)]
print(cycle(7))
print(inv_cycle(7))


def return_graph(n):
    pass  # replace this with your code


def random_step(adj, v):
    pass  # replace this with your code


def walk_histogram(adj):
    pass  # replace this with your code


def cover_time(adj):
    pass  # replace this line with ONE LINE ONLY


############
# QUESTION 3
############

# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selection_sort(lst):
    """ sort lst (in-place) """
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None


def generate_sorted_blocks(lst, k):
    pass  # replace this with your code


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


# c
def merge_sorted_blocks(lst):
    pass  # replace this with your code


def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find_missing(lst, n):
    pass  # replace this with your code


def find(lst, s):
    pass  # replace this with your code


def find2(lst, s):
    pass  # replace this with your code


############
# QUESTION 5
############

# a
def string_to_int(s):
    pass  # replace this with your code


# b
def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    pass  # replace this with your code


# c
def sort_strings1(lst, k):
    pass  # replace this with your code


# e
def sort_strings2(lst, k):
    pass  # replace this with your code


########
# Tester
########

def test():
    # q2
    if complete_graph(4) != \
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]:
        print("error in complete_graph")

    if cycle(5) != \
            [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]:
        print("error in cycle")

    if sum(sum(random_graph(100, 0.8)[i]) for i in range(100)) < 200:
        print("error in random_graph")

    if inv_cycle(13) != \
            [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], \
             [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0], \
             [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], \
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
             [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
             [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0], \
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], \
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], \
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]:
        print("error in inv_cycle")

    if return_graph(5) != \
            [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], \
             [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0]]:
        print("error in return_graph")

    A = random_graph(100, 0.9)
    for _ in range(10):
        v = random.randint(0, 99)
        u = random_step(A, v)
        if not A[v][u]:
            print("error in random_step")

    if 0 in walk_histogram(inv_cycle(13)) or \
            0 in walk_histogram(cycle(10)):
        print("error in walk_histogram")

    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    missing = find_missing([0, 1, 2, 3, 5], 5)
    if missing != 4:
        print("error in find_missing")

    pos = find([30, 40, 50, 60, 10, 20], 60)
    if pos != 3:
        print("error in find")

    pos = find([30, 40, 50, 60, 10, 20], 0)
    if pos != None:
        print("error in find")

    pos = find2([30, 40, 50, 60, 60, 20], 60)
    if pos != 3 and pos != 4:
        print("error in find2")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")