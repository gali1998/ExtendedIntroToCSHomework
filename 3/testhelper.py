from  skeleton import *

def get_random_string(k):
    rand_string = ""
    letters = ["a", "b", "c", "d"]

    return rand_string.join(random.choice(letters) for i in range(k))

def rotate(L, k):
    n = len(L)
    return L[k%n:] + L[:k%n]

def create_random_list():
    n = random.randrange(1, 100)

    lst = [random.randrange(-100, 100) for i in range(n)]

    return lst

def create_random_sorted_list():
    lst = create_random_list()
    lst.sort()

    return lst

def get_random_rotated_list():
    k = random.randrange(1, 500)
    lst = create_random_sorted_list()

    return rotate(lst, k)