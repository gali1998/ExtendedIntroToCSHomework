# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).


import random


############
# QUESTION 2
############

def bar_cycle(n):

    lst = [[] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            
            if j == i + 1 or j == i - 1:
                lst[i].append(1)
            else:
                lst[i].append(0)
                
    lst[0][n-1] = 1
    lst[n-1][0] = 1
        
    return lst


def bar_complete_graph(n):

    return [[1] * n] * n



def bar_random_graph(n, p):

    lst = []

    for i in range(n):
        
        lst.append([random.choices([1,0],[p,1-p])[0] for i in range(n)])

    return lst

def bar_inv_cycle(n):

    lst = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):

            if i != 0:
                if (j == (i**(n-2)) % n) or (j == i + 1 or j == i - 1):
                    lst[i].append(1)
                else:
                    lst[i].append(0)

            else:
                if j == 0 or j == 1 or j == n-1:
                    lst[0].append(1)
                else:
                    lst[0].append(0)

            
    lst[n-1][0] = 1

    return lst

def return_graph(n):

    lst = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):

            if i != 0 and j == 0:
                lst[i].append(1)
                
            else:
                if j == i + 1:
                    lst[i].append(1)
                else:
                    lst[i].append(0)

    return lst


def random_step(adj, v):

    n = len(adj[0])
    lst = []
    
    for i in range(n):
        if adj[v][i] == 1:
            lst.append(i)

    return random.choice(lst)


def walk_histogram(adj):

    lst = [0]*len(adj)
    i = 0   
    while 0 in lst:

        lst[i] += 1

        i = random_step(adj,i)
            
    return lst


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
    sub = []
    result = []

    for i in lst:
        sub.append(i)

        if len(sub) == k:
            selection_sort(sub)
            result.append(sub)
            sub = []

    if len(sub) != 0:
        selection_sort(sub)
        result.append(sub)

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

    result = []
    n = len(lst)

    if n == 1:
        return lst[0]
    else:
        for i in range(0, n, 2):

            if i + 1 < n:
                result.append(merge(lst[i],lst[i+1]))
            else:
                result.append(lst[i])

        return merge_sorted_blocks(result)


def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find_missing(lst, n):

    start = 0
    end = n-1

    while True:
        
        if start == n-1 and start == lst[n-1]:
            return start + 1
        
        if start == end:
            return start
        
        if (end - start + 1) % 2 != 0:
            if (start + end)//2 == lst[(start + end)//2]:

                start = (start + end)//2 + 1
                
            else:
                end = (start + end)//2


        else:
            if (start + end)//2 == lst[(start + end)//2]:
                if (start + end + 1)//2 != lst[(start + end + 1)//2]:
                    return (start + end + 1)//2

                else:
                    start = (start + end + 1)//2

            else:
                end = (start + end)//2


def find(lst, s):
    n = len(lst)
    start = 0
    end = n - 1
    middle = (start + end)//2

    while lst[middle] >= lst[middle - 1]:
        start = middle + 1
        middle = (start + end)//2
        if start == end:
            start = n
            break

    rotation_index = middle

    if lst[n-1] == s:
        return n-1

    if lst[0] > s:
        left = rotation_index - 1
        right = n-1
        
    else:
        left = 0
        right = rotation_index - 1
        
    while left <= right:
        middle2 = (right + left)//2
        if s == lst[middle2]:
            return middle2
        elif s < lst[middle2]:
            right = middle2 - 1
        else:
            left = middle2 + 1
            
    return None


def find2(lst, s):

    for i in range(len(lst)):

        if lst[i] == s:
            return i
    else:
        return None
            
############
# QUESTION 5
############

# a
def string_to_int(s):

    dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
    cnt = 0
    pwr = len(s) - 1
    
    for i in s:

        cnt += (dic[i])*(5**pwr)
        pwr = pwr - 1

    return cnt



# b
def bar_int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1

    dic = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e'}
    string = ''
 
    while len(string)!= k:

        string += dic[n % 5]

        n = n//5

    return string[::-1]

# c
def bar_sort_strings1(lst, k):

    lst_of_num = []
    result = []
    lst_comp = [0]*(5**k)

    for s in lst:
        
        a = string_to_int(s)
        lst_of_num.append(a)
        lst_comp[a] += 1


    for index, i in enumerate (lst_comp):

        if i > 0:
            result.extend([bar_int_to_string(k, index)]*i)

    return result
    



# e
def bar_sort_strings2(lst, k):

    result = []

    for i in range(5**k):
        for j in lst:
            if(bar_int_to_string(k,i) == j):
                result.append(j)

    return result



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
    missing = find_missing([0,1,2,3,5], 5)
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

