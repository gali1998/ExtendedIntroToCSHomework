# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).


import random

############
# QUESTION 2
############

def verify_size(n):
    if n < 2:
        raise ValueError('Cannot create cycle smaller than 2')

def idan_cycle(n):
    verify_size(n)
    cycle_matrix = []
    for i in range(n):
        cycle_matrix.append([0]*n)
        next_neighbor_index = (i + 1)%n
        last_neighbor_index = i - 1
        cycle_matrix[i][next_neighbor_index] = 1
        cycle_matrix[i][last_neighbor_index] = 1
    return cycle_matrix


def idan_complete_graph(n):
    verify_size(n)
    comp_matrix = []
    for i in range(n):
        comp_matrix.append([1]*n)
    return comp_matrix

def idan_random_graph(n, p):
    verify_size(n)
    if p < 0 or p > 1:
        raise ValueError("Given p probability is not valid (not between 0 and 1")
    random.seed()
    rand_matrix = []
    for i in range(n):
        row = []
        for k in range(n):
            row.append(0)
            r = random.random()
            if r < p:
                row[k] = 1
        rand_matrix.append(row)
    return rand_matrix

def idan_inv_cycle(n):
    verify_size(n)
    matrix = idan_cycle(n)
    for x in range(1, n):
        inv = (x**(n - 2))%n
        matrix[x][inv] = 1
    matrix[0][0] = 1
    return matrix


def idan_return_graph(n):
    verify_size(n)
    matrix = []
    for i in range(n):
        next_node = (i + 1)%n
        matrix.append([0]*n)
        matrix[i][next_node] = 1
        if i > 0:
            matrix[i][0] = 1
    return matrix


def idan_random_step(adj, v):
    if v > len(adj) or v < 0:
        raise ValueError('Bad vertex given (out of bounds): ', v)
    neighbors = list(filter(lambda i: adj[v][i] == 1, range(len(adj))))
    random.seed()
    return random.choice(neighbors)

def idan_walk_histogram(adj):
    curr_vertex = 0
    unstepped = len(adj) - 1
    hist = [0]*len(adj)
    hist[0] = 1
    while unstepped > 0:
        curr_vertex = idan_random_step(adj, curr_vertex)
        if hist[curr_vertex] == 0:
            unstepped -= 1
        hist[curr_vertex] += 1
    return hist

def idan_cover_time(adj):
    return sum(idan_walk_histogram(adj))# replace this line with ONE LINE ONLY

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

def idan_generate_sorted_blocks(lst, k):
    n = len(lst)
    sublists = []
    for i in range(0, n, k):
        block = lst[i:i + k]
        selection_sort(block)
        sublists.append(block)
    return sublists

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
def idan_merge_sorted_blocks(lst):
    m = len(lst)
    if m == 0:
        return []
    if m == 1:
        return lst[0]
    while m > 1:
        merged_blockes = []
        for i in range(0, m, 2):
            if i + 1 < m:
                merged_blockes.append(merge(lst[i], lst[i+1]))
            else:
                merged_blockes.append(lst[i])
        lst = merged_blockes
        m = len(merged_blockes)
    return merged_blockes[0]

def idan_sort_by_block_merge(lst, k):
    return idan_merge_sorted_blocks(idan_generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def idan_find_missing(lst, n):
    first_discrepency = n
    if n%2 == 0:
        n = n-1
        if lst[n] > n:
            first_discrepency = n
    i = n//2
    while n >= 1:
        if lst[i] > i:
            first_discrepency = i
            i = i-n//2
        else:
            i = i+n//2
        n = n // 2
    return first_discrepency


def idan_find(lst, s):
    n = len(lst)
    if n%2 == 0 and n > 0:
        n = n-1
        if lst[n] == s:
            return n
    k = idan_find_k_addition_factor(lst)
    i = (n//2 -k) % n
    while n >= 1:
        if lst[i] == s:
            return i
        if lst[i] < s:
            i = (i + n // 2) % n
        elif lst[i] > s:
            i = (i - n // 2) % n
        n = n // 2
    return None

def idan_find_k_addition_factor(lst):
    """ This function, given a k rotated list of length n,
    finds a parameter k such that for every index I in lst, lst[(I+k)%n] = sorted(lst[i])"""
    n = len(lst)
    top_limit = n-1
    if n%2 == 0:
        n = n-1
        if lst[0] < lst[n]:
            return 0
    i = n//2
    bottom_limit = 0
    n = 2*n
    while n >= 1:
        if lst[i] > lst[(i+1)%len(lst)]:
            return (i+1)%len(lst)
        else:
            if lst[i] > lst[top_limit]:
                bottom_limit = i
            elif lst[i] < lst[bottom_limit]:
                top_limit = i
            i = (top_limit + bottom_limit) // 2
        n = n//2
    return 0

def idan_find2(lst,s):
    n = len(lst)
    top_limit = n - 1
    bottom_limit = 0
    if n % 2 == 0 and n > 0:
        n = n - 1
        if lst[n] == s:
            return n
    i = (top_limit + bottom_limit) // 2
    n = 2 * n
    while n >= 1:
        if lst[i] == s:
            return i
        while top_limit != bottom_limit and i != top_limit and lst[top_limit] == lst[bottom_limit] and lst[top_limit] == lst[i]:
            top_limit -= 1
            bottom_limit -= 1
            n -= 2
        if lst[i] < s:
            if lst[top_limit] < s:
                if lst[i] < lst[top_limit]:
                    top_limit = i
                elif lst[top_limit] <= lst[i]:
                    bottom_limit = i
            elif s <= lst[top_limit]:
                bottom_limit = i
                if top_limit - bottom_limit == 1:
                    bottom_limit = top_limit
        elif s < lst[i]:
            if s < lst[bottom_limit]:
                if lst[i] < lst[bottom_limit]:
                    top_limit = i
                elif lst[bottom_limit] <= lst[i]:
                    bottom_limit = i
            elif lst[bottom_limit] <= s:
                top_limit = i
        i = (top_limit + bottom_limit) // 2
        n = n // 2
    return None



############
# QUESTION 5
############

# a
def idan_string_to_int(s):
    k = len(s)
    str_value = 0
    values_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    for i in range(k):
        str_value *= 5
        str_value += values_dict[s[i]]
    return str_value

# b
def idan_int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    values_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
    str = ''
    for i in range(k):
        str = values_dict[n%5] + str
        n = n//5
    return str

# c
def idan_sort_strings1(lst, k):
    aid_list = get_aid_list(k)
    sorted_list = []
    index_dict = dict()
    for s in lst:
        s_val = idan_string_to_int(s)
        if s_val not in index_dict:
            index_dict[s_val] = 0
        index_dict[s_val] += 1
    for i in range(len(aid_list)):
        if i in index_dict:
            for m in range(index_dict[i]):
                sorted_list.append(aid_list[i])
    return sorted_list

def get_aid_list(k):
    char_list = ['a', 'b', 'c', 'd', 'e']
    if k == 1:
        return char_list
    else:
        last_aid_list = get_aid_list(k-1)
        aid_list = []
        for s in last_aid_list:
            for c in char_list:
                aid_list.append(s + c)
        return aid_list

# e
def idan_sort_strings2(lst, k):
    sorted_list = []
    for i in range(0,5**k):
        for s in lst:
            if idan_string_to_int(s) == i:
                sorted_list.append(s)
    return sorted_list


########
# Tester
########

def test():
    # q2
    if idan_complete_graph(4) != \
           [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]:
        print("error in complete_graph")

    if idan_cycle(5) != \
           [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]:
        print("error in cycle")

    if sum(sum(idan_random_graph(100, 0.8)[i]) for i in range(100)) < 200:
        print("error in random_graph")

    if idan_inv_cycle(13) != \
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

    if idan_return_graph(5) != \
       [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], \
        [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0]]:
        print("error in return_graph")

    A = idan_random_graph(100, 0.9)
    for _ in range(10):
        v = random.randint(0, 99)
        u = idan_random_step(A, v)
        if not A[v][u]:
            print("error in random_step")

    if 0 in idan_walk_histogram(idan_inv_cycle(13)) or \
       0 in idan_walk_histogram(idan_cycle(10)):
        print("error in walk_histogram")

    
    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if idan_generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if idan_generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if idan_generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if idan_merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print(idan_merge_sorted_blocks(block_lst1))
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if idan_merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    missing = idan_find_missing([0,1,2,3,5], 5)
    if missing != 4:
        print("error in find_missing")

    pos = idan_find([30, 40, 50, 60, 10, 20], 60)
    if pos != 3:
        print("error in find")

    pos = idan_find([30, 40, 50, 60, 10, 20], 0)
    if pos != None:
        print("error in find")

    pos = idan_find2([30, 40, 50, 60, 60, 20], 60)
    if pos != 3 and pos != 4:
        print(idan_find2([30, 40, 50, 60, 60, 20], 60))
        print("error in find2")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = idan_int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (idan_string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if idan_sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print(idan_sort_strings1(lst1, 4))
        print("error in sort_strings1")

    if idan_sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")
