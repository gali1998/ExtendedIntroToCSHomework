from skeleton import *
import random

def get_random_string():
    length = random.randrange(1, 10)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x', 'y','z']

    string = ""
    for i in range(length):
        string += random.choice(letters)
    return string

is_ok = True
for i in range(100):
    s1 = get_random_string()
    s2 = get_random_string()

    if distance( s1, s2) != distance_fast(s1, s2):
        is_ok = False
        print(is_ok)
        break
print(is_ok)
