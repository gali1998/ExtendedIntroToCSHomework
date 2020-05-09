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
        print(str(n) + "," + str(m) + " calls " + str(n)+","+str(m+1-i))
        if not win(n, m  + 1 - i):
            return True
    for i in range(2, n + 1):
        print(str(n) + "," + str(m) + " calls " + str(n+1-i) + "," + str(m ))
        if not win(n + 1 - i,m):
            return True
    return False

# c

def win_fast_mem(n, m, dict):
    key = "n="+str(n)+"m="+str(m)

    if key in dict:
        print(key)
        return dict[key]

    for i in range(2, m + 1):
        print(str(n) + "," + str(m) + " calls " + str(n)+","+str(m+1-i))
        if not win_fast_mem(n, m  + 1 - i, dict):
            dict[key] = True
            return True
    for i in range(2, n + 1):
        print(str(n) + "," + str(m) + " calls " + str(n+1-i) + "," + str(m ))
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
    if s == 0:
        return 1
    if L == []:
        return 0
    with_first = subset_sum_count(L[1:], s-L[0])
    without_first = subset_sum_count(L[1:], s)

    return with_first + without_first



def subset_sum_search_all(L, s):
    if s == 0:
        return [[]]

    result = []
    i=0
    while i < len(L):
        sublist = subset_sum_search_from_index(L, s, i, [])

        if sublist != []:
            result.append(sublist)
        else:
            i += 1
        i += len(sublist)

    return  result

def subset_sum_search_from_index(L, s, i, result):
    if s == 0:
        return result
    if i == len(L):
        print("s")
        return []
    with_first = subset_sum_search_from_index(L, s-L[i], i + 1, result + [L[i]])
    without_first = subset_sum_search_from_index(L, s, i + 1, result)

    if with_first == []:
        return without_first
    return  with_first

print("%%%%%%%%%%%%")
L = [3, 2]

#print(subset_sum_search_from_index([1,2], 6, 1, []))
print(subset_sum_search_all([], 0))
print("%%%%%%%%%%%%")

############
# QUESTION 6
############

def distance(s1, s2):
    print("called with " +s1+","+s2)
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    len_s1 = len(s1)
    len_s2 = len(s2)
    if s1[len_s1 - 1] == s2[len_s2 - 1]:
        return distance(s1[:len_s1 - 1], s2[:len_s2 - 1])
    else:
        distance_insert = distance(s1, s2[:len_s2 - 1])
        distance_remove = distance(s1[: len_s1 - 1], s2)
        distance_replace = distance(s1[:len_s1 - 1], s2[: len_s2 - 1])
        return 1 + min(distance_insert, distance_remove, distance_replace)

def distance_fast(s1, s2):
    distances = [[-1 for j in range(len(s2))] for i in range(len(s1))]

    return distance_mem(s1, s2, distances)

def distance_mem(s1, s2, distances):
    print("called with " +s1+","+s2)
    len1 = len(s1)
    len2 = len(s2)

    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

    if distances[len1 - 1][len2 -1] != -1:
        return distances[len1 - 1][len2 -1]
    if s1[len1-1] == s2[len2-1]:
        distances[len1-1][len2-1] = distance_mem(s1[:len1-1], s2[:len2-1], distances)

        return distances[len1-1][len2-1]
    distance_insert = distance_mem(s1, s2[:len2 - 1], distances)
    distance_remove = distance_mem(s1[: len1 - 1], s2, distances)
    distance_replace = distance_mem(s1[:len1 - 1], s2[: len2 - 1], distances)

    distances[len1-1][len2-1] = 1 + min(distance_insert, distance_remove, distance_replace)

    return distances[len1-1][len2-1]
print("---------------------------------")
print(distance_fast("ab", "cd"))
print(distance("ab", "cd"))
print("---------------------------------")

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



