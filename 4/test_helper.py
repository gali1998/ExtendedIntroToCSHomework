import itertools
import  random

def get_random_string():
    length = random.randrange(1, 10)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x', 'y','z']

    string = ""
    for i in range(length):
        string += random.choice(letters)
    return string

def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t) + 1,
               levenshtein(s, t[:-1]) + 1,
               levenshtein(s[:-1], t[:-1]) + cost])

    return res

def get_random_list():
    options = [i for i in range(-101, 101)]

    length = random.randrange(1, 20)

    L = []

    for i in range(length):
        value = random.choice(options)
        L.append(value)
        options.remove(value)

    return L


def get_all_sublists(L):
    result = []
    for i in range(len(L) + 1):
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