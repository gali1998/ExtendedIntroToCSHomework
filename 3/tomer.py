# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).


import random


############
# QUESTION 2
############
###############################################################################3  
def avgcovertime(func):
    import time
    sum1=0
    sumt=0
    for i in range(10):
        t0= time.perf_counter()
        sum1+=tomer_cover_time(func)
        t1= time.perf_counter()
        sumt+=(t1-t0)
    
    print(sum1/10)
    print((sumt)/10)
######################################################################################
    
def tomer_cycle(n):
    lst=[]
    for i in range(n):
        lst.append([])
        for j in range(n):
            if j-1 ==i or j+1==i:
                lst[i].append(1)
            elif i-j == n-1 or i-j==1-n:
                lst[i].append(1)
            else:
                lst[i].append(0)
    return lst

def tomer_complete_graph(n):
    return [[1 for i in range(n)] for j in range(n)]

def tomer_random_graph(n, p):
    lst=[]
    for i in range(n):
        lst.append([])
        for j in range(n):
            if random.random()<=p:
                lst[i].append(1)
            else:
                lst[i].append(0)
    return lst
        

def tomer_inv_cycle(n):
    lst = []
    for i in range(n):
        lst.append([])
        for j in range(n):
            if j - 1 == i or j + 1 == i or i - j == n - 1 or i - j == 1 - n or (j ** (n - 2)) % n == i or (
                    i == j and i == 0):
                lst[i].append(1)
            else:
                lst[i].append(0)
    return lst

def tomer_return_graph(n):
    return [[1 if (j == i+1 or j==0) and i!=j  else 0 for j in range(n)]for i in range(n)]

def tomer_random_step(adj, v):
    n_lst=[]
    for i in range(len(adj)):
        if adj[v][i]==1:
            n_lst.append(i)
    return random.choice(n_lst)

def tomer_walk_histogram(adj):
    next_step = 0
    n_lst=[1]
    count=1
    for i in range(1,len(adj)):
        n_lst.append(0)
    while count!=len(adj):
        next_step= tomer_random_step(adj,next_step)
        if n_lst[next_step]==0:
            count+=1
        n_lst[next_step]+=1
    return n_lst

def tomer_cover_time(adj):
    return sum(tomer_walk_histogram(adj))

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


def tomer_generate_sorted_blocks(lst, k):
    r_lst=[]
    if len(lst)/k==len(lst)//k:
        n= int(len(lst)/k)
    else:
        n= int(len(lst)//k+1)
    for i in range(n):
        r_lst.append(lst[i*k:(i+1)*k])
        selection_sort(r_lst[i])
    return r_lst
        


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
def tomer_merge_sorted_blocks(lst):
    n= len(lst)
    return merge_sorted_blocks_afterenvelope(lst,0,n)

def merge_sorted_blocks_afterenvelope(lst,start,end):
    if end-start == 1:
        return lst[start]
    else:
        return merge(merge_sorted_blocks_afterenvelope(lst,start,(end+start)//2),merge_sorted_blocks_afterenvelope(lst,(end+start)//2,end))
    
def tomer_sort_by_block_merge(lst, k):
    return tomer_merge_sorted_blocks(tomer_generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def tomer_find_missing(lst, n):
    left = 0
    right = n-1
    while left <=right:
        middle = (right+left)//2
        if lst[middle]== middle+1:
            if  middle == 0 or lst[middle-1] == middle -1 :
                return middle
            else:
                right = middle-1
        else:
            if middle ==n-1 or lst[middle+1]!=middle+1:
                return middle+1
            else:
                left = middle +1
    return None
            



def tomer_find(lst, s):
    left = 0
    right = len(lst)-1
    while left<= right:
        middle = (right+left)//2
        if lst[middle] == s:
            return middle
        if lst[right]==s:
            return right
        if (lst[middle]>s and lst[right]>s and lst[right]<lst[middle]) or(lst[middle]<s and lst[right]>s)or (lst[middle]<s and lst[right]<s and lst[right]<lst[middle]):
            left = middle+1
        else:
            right = middle -1
    return None
####################################################################################################################
def tomer_checkfind2():
    lst=[]
    for i in range(1000):
        if i!=654:
            lst.append(8)
        else:
            lst.append(9)
    return find2(lst,9)
def tomer_checkfind():
    lst=[]
    for i in range(100):
        for j in range(random.randint(1,200)):
            lst.append(i)
    for i in range(len(lst)):
        lm = rotate(lst,i)
       # print(lm)
        for j in range(len(lm)):
            z=find2(lm,j)
            if find2(lm,j)!= None:
                if not(j==lm[z]):
                    print("error")
            else:
                if (j in lm):
                    print("error")
                    break
    
                  
def rotate(l,k):
    n = len(l)
    return l[k%n:]+l[:k%n]
 ####################################################################################################

def tomer_find2(lst, s):
    left = 0
    right = len(lst)-1
    while left<= right:
        middle = (right+left)//2
        if lst[middle] == s:
            return middle
        if lst[right]==s:
            return right
        if (lst[middle]>s and lst[right]>s and lst[right]<lst[middle]) or(lst[middle]<s and lst[right]>s)or (lst[middle]<s and lst[right]<s and lst[right]<lst[middle]):
            left = middle+1
        elif lst[middle] == lst[right] and lst[middle]==lst[left]:
            left+=1
            right-=1
        else:
            right = middle -1
    return None


############
# QUESTION 5
############

# a
def tomer_string_to_int(s):
    num=0
    dict1 = {"a":0,"b":1,"c":2,"d":3,"e":4}
    for n_power, char in enumerate(s):
        num+= dict1[char]*(5**(len(s)-1-n_power))
    return num


# b
def tomer_int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    dict1 = {0:"a",1:"b",2:"c",3:"d",4:"e"}
    s=""
    for i in range(0,k):
        s+=dict1[n//(5**(k-i-1))]
        n-=(n//5**(k-i-1))*5**(k-i-1)
    return s
        
def tomer_check_int_to_string():
    for i in range(5**3):
        if tomer_string_to_int(tomer_int_to_string(3,i))!=i:
            print("prob",i)
    a= ["a","b","c","d","e"]
    lst=[x+y+z for  x in a for y in a for z in a]
    for item in lst:
        #print (item)
        if tomer_int_to_string(3,tomer_string_to_int(item))!= item:
            print("prob",i)

###############################################################
# c
def sort_strings1(lst, k):
    n= len(lst)
    r_lst=[]
    k5_lst=[]
    for i in range(5**k):
        k5_lst.append(0)
    for i in range(n):
        k5_lst[tomer_string_to_int(lst[i])]+=1
    for i in range(5**k):
        if k5_lst[i]!= 0:
            for j in range(k5_lst[i]):
                r_lst.append(tomer_int_to_string(k,i))
    return r_lst
    
##################################################################
# e
def sort_strings2(lst, k):
    r_lst=[]
    for i in range(5**k):
        for j in lst:
            if tomer_string_to_int(j)==i:
                r_lst.append(j)
    return r_lst
                


########
# Tester
########

def test():
    # q2
    if tomer_complete_graph(4) != \
           [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]:
        print("error in complete_graph")

    if tomer_cycle(5) != \
           [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]:
        print("error in cycle")

    if sum(sum(tomer_random_graph(100, 0.8)[i]) for i in range(100)) < 200:
        print("error in random_graph")

    if tomer_inv_cycle(13) != \
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

    if tomer_return_graph(5) != \
       [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], \
        [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0]]:
        print("error in return_graph")

    A = tomer_random_graph(100, 0.9)
    for _ in range(10):
        v = random.randint(0, 99)
        u = tomer_random_step(A, v)
        if not A[v][u]:
            print("error in random_step")

    if 0 in tomer_walk_histogram(tomer_inv_cycle(13)) or \
       0 in tomer_walk_histogram(tomer_cycle(10)):
        print("error in walk_histogram")

    
    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if tomer_generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if tomer_generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if tomer_generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if tomer_merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if tomer_merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    missing = tomer_find_missing([0,1,2,3,5], 5)
    if missing != 4:
        print("error in find_missing")

    pos = tomer_find([30, 40, 50, 60, 10, 20], 60)
    if pos != 3:
        print("error in find")

    pos = tomer_find([30, 40, 50, 60, 10, 20], 0)
    if pos != None:
        print("error in find")

    pos = tomer_find2([30, 40, 50, 60, 60, 20], 60)
    if pos != 3 and pos != 4:
        print("error in find2")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = tomer_int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (tomer_string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")

