from  hw3_207704842 import *

def get_random_string(k):
    rand_string = ""
    letters = ["a", "b", "c", "d"]

    return rand_string.join(random.choice(letters) for i in range(k))

def rotate(L, k):
    n = len(L)
    return L[k%n:] + L[:k%n]

def create_random_list():
    n = random.randrange(1, 10)
    lst = []

    for i in range(n):
        val = random.randrange(-100, 100)

        while val in lst:
            val = random.randrange(-100, 100)

        lst.append(val)

    return lst

def creaste_rotated_random_list_not_unique():
    lst = create_random_sorted_list()

    result = []

    for i in lst:
        repetitions = random.randrange(1,20)

        for l in range(repetitions):
            result.append(i)

    k = random.randrange(1, 500)

    return rotate(result, k)

def create_random_sorted_list():
    lst = create_random_list()
    lst.sort()

    return lst

def get_random_rotated_list():
    k = random.randrange(1, 500)
    lst = create_random_sorted_list()

    return rotate(lst, k)