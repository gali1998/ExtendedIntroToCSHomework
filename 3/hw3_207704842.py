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
    return (i - j == 1 or i - j == - 1 or (i == n-1 and j == 0) or (j == n-1 and i == 0))

def cycle(n):
    return [[1 if isInCycle(i, j, n) else 0 for j in range(n)] for i in range(n)]

def complete_graph(n):
    return [[1 for j in range(n)] for i in range(n)]

def random_graph(n, p):
    return [[1 if random.random() <= p else 0 for j in range(n)] for i in range(n)]

def inv_cycle(n):
    return [[1 if isInCycle(i, j, n) or j == (i**(n-2) % n) or (i == 0 and j == 0) else 0 for j in range(n)] for i in range(n)]

def return_graph(n):
    return [[1 if (j == 1 + i or (i != 0 and j == 0)) else 0 for j in range(n)] for i in range(n)]

def random_step(adj, v):
    neighbours = []

    for i in range(len(adj[v])):
        if adj[v][i] == 1:
            neighbours.append(i)

    return random.choice(neighbours)

def walk_histogram(adj):
    histogram = [0] * len(adj)
    countDifferentValues = 0
    curremtNode = 0

    while countDifferentValues < len(adj):
        if histogram[curremtNode] == 0:
            countDifferentValues += 1

        histogram[curremtNode] += 1

        curremtNode = random_step(adj, curremtNode)

    return histogram


def cover_time(adj):
    return sum(walk_histogram(adj))


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
    result = []

    for i in range(0, len(lst), k):
        sublist = lst[i: i + k].copy()
        selection_sort(sublist)
        result.append(sublist)

    return result


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
    if len(lst) == 0:
        return []
    while(len(lst) > 1):
        if len(lst) % 2 != 0:
            lst[-2] = merge(lst[-2], lst[-1])
            lst.pop()
        lst = [merge(lst[i], lst[i + 1]) for i in range(0, len(lst) - 1, 2)]

    return lst[0]

def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find_missing(lst, n):
    left = 0
    right = n

    while left < right:
        middle = (right + left) // 2

        if lst[middle] > middle:
            right = middle
        else:
            left = middle + 1

    return right


def find_pivot(lst):
    """returns x such as lst is sorted from 0 to x"""
    left = 0
    right = len(lst)

    while(left < right):
        middle = (left + right) // 2

        if lst[left] < lst[middle]:
            left = middle
        else:
            right = middle
    return right

def binary_search(lst, key, start, stop):
    """ iterative binary search
        lst better be sorted for binary search to work """
    n = stop + 1
    left = start
    right = n-1

    while left <= right:
        middle = (right+left)//2 # middle rounded dow
        if key == lst[middle]:   # item found
            return middle
        elif key < lst[middle]:  # item cannot be in top half
            right = middle-1
        else:                    # item cannot be in bottom half
            left = middle+1

    return None

def find(lst, s):
    if len(lst) == 0:
        return None
    pivot = find_pivot(lst)

    if s >= lst[0] and s <= lst[pivot]:
        return binary_search(lst, s, 0, pivot)
    else:
        return binary_search(lst, s, pivot + 1, len(lst))

def find2(lst, s):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == s:
            return middle

        elif lst[left] == lst[middle] and lst[middle] == lst[right]:
            left += 1
            right -= 1

        elif lst[left] <= lst[middle]:
            if lst[left] <= s and s < lst[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if lst[middle] < s and s <= lst[right]:
                left = middle + 1
            else:
                right = middle

    return None

############
# QUESTION 5
############

# a
def string_to_int(s):
    letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    result = 0
    length = len(s)

    for i in range(length):
        value = letters[s[length-i-1]]

        result = (5**(i)*value) + result

    return result

# b
def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    numbers = {0: "a", 1: "b", 2 : "c", 3: "d", 4: "e"}
    result = ""

    for i in range(k):
        result += numbers[n % 5]

        n = n // 5

    return result[::-1]

# c
def sort_strings1(lst, k):
    sorted_list = []
    help_list = [0 for i in range(5**k)]

    for string in lst:
        number = string_to_int(string)
        help_list[number] += 1

    for i in range(5**k):
        if help_list[i] != 0:
            string = int_to_string(k, i)

            for j in range(help_list[i]):
                sorted_list.append(string)

    return sorted_list
# e
def sort_strings2(lst, k):
    sorted_list = []

    for i in range(5**k):
        for sublist in lst:
            if i == string_to_int(sublist):
                sorted_list.append(sublist)

    return sorted_list


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
