import itertools
import  random
def get_random_list():
    options = [i for i in range(0, 101)]

    length = random.randrange(1, 20)

    L = []

    for i in range(length):
        value = random.choice(options)
        L.append(value)
        options.remove(value)

    return L


def get_all_sublists(L):
    result = []
    for i in range(len(L)):
        all_sublists = itertools.combinations(L, i)
        for t in all_sublists:
            result.append(list(t))

    return result

def get_all_sublists_with_sum(L, s):
    result = []

    for sublist in L:
        if sum(sublist) == s:
            result.append(sublist)


def count_all_sublists_with_sum(L, s):
    count = 0

    for sublist in L:
        if sum(sublist) == s:
            count += 1

    return count