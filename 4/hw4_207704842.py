# Skeleton file for HW4 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).


############
# QUESTION 2
############

# a
def win(n, m):
    if n == 0 and m == 0:
        return True
    if n == 1 and m == 1:
        return False

    for i in range(2, m + 1):
        if not win(n, m  + 1 - i):
            return True
    for i in range(2, n + 1):
        if not win(n + 1 - i,m):
            return True
    return False

# c

def win_fast_mem(n, m, dict):
    key = "n="+str(n)+"m="+str(m)

    if key in dict:
        return dict[key]

    for i in range(2, m + 1):
        if not win_fast_mem(n, m  + 1 - i, dict):
            dict[key] = True
            return True
    for i in range(2, n + 1):
        if not win_fast_mem(n + 1 - i,m, dict):
            dict[key] = True
            return True
    dict[key] = False
    return False

def win_fast(n, m):
    dict = {"n=0m=0": True, "n=1m=1": False}

    return win_fast_mem(n, m, dict)

############
# QUESTION 3
############

# b

def is_in_inverse(n, i, j):
    size_of_block = pow(2, n-1)

    return (i >= size_of_block) and (j >= size_of_block)

def had_local(n, i, j):
    if n == 0:
        return 0
    size = pow(2, n-1)

    if is_in_inverse(n, i, j):
        return 1 - had_local(n-1, i - size, j - size)
    if i >= size:
        i = i - size

    if j >= size:
        j = j - size

    return had_local(n-1, i, j)

# d
had_complete = lambda n: [[had_local(n, i, j) for j in range(2**n)] for i in range(2**n)]


############
# QUESTION 4
############

def subset_sum_count(L, s):
    return subset_sum_count_with_index(L, 0, s)

def subset_sum_count_with_index(L, index, s):
    if s == 0 and index == len(L):
        return 1
    if index == len(L):
        return 0

    first = index
    with_first = subset_sum_count_with_index(L, index + 1, s - L[first])
    without_first = subset_sum_count_with_index(L, index + 1, s)

    return with_first + without_first

def subset_sum_search_all(L, s):
    return subset_sum_search_all_with_index(L, 0, s)

def subset_sum_search_all_with_index(L, index, s):
    if s == 0 and index == len(L):
        return [[]]
    if index == len(L):
        return []

    first = index
    with_first = subset_sum_search_all_with_index(L, index + 1, s - L[first])
    without_first = subset_sum_search_all_with_index(L, index + 1, s)

    if with_first != []:
        add_value_to_all_sublists(with_first, L[first])

    return with_first + without_first

def add_value_to_all_sublists(L, value):
    for sublist in L:
        sublist.append(value)

    return L

############
# QUESTION 6
############

def distance(s1, s2):
    return distance_with_index(s1, s2, len(s1), len(s2))

def distance_with_index(s1, s2, index_s1, index_s2):
    if index_s1 == 0:
        return index_s2
    if index_s2 == 0:
        return index_s1

    if s1[index_s1 - 1] == s2[index_s2 - 1]:
        return distance_with_index(s1, s2, index_s1 - 1, index_s2 - 1)
    else:
        distance_insert = distance_with_index(s1, s2, index_s1, index_s2 - 1)
        distance_remove = distance_with_index(s1, s2, index_s1 - 1, index_s2)
        distance_replace = distance_with_index(s1, s2, index_s1 - 1, index_s2 - 1)

        return 1 + min(distance_insert, distance_remove, distance_replace)


def distance_fast(s1, s2):
    distances = [[-1 for j in range(len(s2))] for i in range(len(s1))]

    return distances_mem_with_index(s1, s2, len(s1), len(s2), distances)


def distances_mem_with_index(s1, s2, index_s1, index_s2, distances):
    if index_s1 == 0:
        return index_s2
    if index_s2 == 0:
        return index_s1
    if distances[index_s1 - 1][index_s2 - 1] != -1:
        return distances[index_s1 - 1][index_s2 - 1]
    if s1[index_s1 - 1] == s2[index_s2 - 1]:
        distances[index_s1 - 1][index_s2 - 1] = distances_mem_with_index(s1, s2, index_s1 - 1, index_s2 - 1, distances)

        return distances[index_s1 - 1][index_s2 - 1]
    distance_insert = distances_mem_with_index(s1, s2, index_s1, index_s2 - 1, distances)
    distance_remove = distances_mem_with_index(s1, s2, index_s1 - 1, index_s2, distances)
    distance_replace = distances_mem_with_index(s1, s2, index_s1 - 1, index_s2 - 1, distances)

    distances[index_s1 - 1][index_s2 - 1] = 1 + min(distance_insert, distance_remove, distance_replace)

    return distances[index_s1 - 1][index_s2 - 1]

########
# Tester
########

def test():
    if win(3, 3) != False or \
            win(3, 4) != True or \
            win(1, 1) != False or \
            win(1, 2) != True:
        print("Error in win()")

    if win_fast(3, 3) != False or \
            win_fast(3, 4) != True or \
            win_fast(1, 1) != False or \
            win_fast(1, 2) != True:
        print("Error in win_fast()")

    contains = lambda L, R: all(R.count(r) <= L.count(r) for r in R)
    L = [1, 2, 4, 8, 16]

    if subset_sum_count(L, 13) != 1 or subset_sum_count(L, 32) != 0 \
            or subset_sum_count([i for i in range(1, 10)], 7) != 5:
        print("Error in subset_sum_count")

    R_lst = subset_sum_search_all(L, 13)
    if R_lst == None:
        print("Error in subset_sum_search_all")
    elif len(set([tuple(sorted(R)) for R in R_lst])) != len(R_lst) or len(R_lst) != 1:
        print("Error in subset_sum_search_all")
    else:
        for R in R_lst:
            if R == None or not sum(R) == 13 or not contains(L, R):
                print("Error in subset_sum_search_all")

    R_lst = subset_sum_search_all(L, 32)
    if not R_lst == []:
        print("Error in subset_sum_search_all")

    L = [i for i in range(1, 10)]
    R_lst = subset_sum_search_all(L, 7)
    if R_lst == None:
        print("Error in subset_sum_search_all")
    elif len(set([tuple(sorted(R)) for R in R_lst])) != len(R_lst) or len(R_lst) != 5:
        print("Error in subset_sum_search_all")
    else:
        for R in R_lst:
            if R == None or not sum(R) == 7 or not contains(L, R):
                print("Error in subset_sum_search_all")

    if distance('computer', 'commuter') != 1 or \
            distance('sport', 'sort') != 1 or \
            distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
        print("Error in distance")

    if distance_fast('computer', 'commuter') != 1 or \
            distance_fast('sport', 'sort') != 1 or \
            distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
        print("Error in distance_fast")



