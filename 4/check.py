from skeleton import *
import random
from test_helper import *


def distances_mem_with_index1(s1, s2, index_s1, index_s2, distances, count):
    if index_s1 == 0:
        return index_s2
    if index_s2 == 0:
        return index_s1
    if distances[index_s1 - 1][index_s2 - 1] != -1:
        print(str(index_s1) + " " + str(index_s2) + "calls")
        return distances[index_s1 - 1][index_s2 - 1]
    if s1[index_s1 - 1] == s2[index_s2 - 1]:
        distances[index_s1 - 1][index_s2 - 1] = distances_mem_with_index1(s1, s2, index_s1 - 1, index_s2 - 1, distances, count)

        return distances[index_s1 - 1][index_s2 - 1]
    print(str(index_s1) + " " + str(index_s2 - 1)+" called by "+ str(index_s1) + " " + str(index_s2))
    distance_insert = distances_mem_with_index1(s1, s2, index_s1, index_s2 - 1, distances, count)
    print(str(index_s1 - 1) + " " + str(index_s2 - 1)+" called by "+ str(index_s1) + " " + str(index_s2))
    distance_remove = distances_mem_with_index1(s1, s2, index_s1 - 1, index_s2, distances, count)
    print(str(index_s1 -1) + " " + str(index_s2)+" called by "+ str(index_s1) + " " + str(index_s2))
    distance_replace = distances_mem_with_index1(s1, s2, index_s1 - 1, index_s2 - 1, distances, count)

    distances[index_s1 - 1][index_s2 - 1] = 1 + min(distance_insert, distance_remove, distance_replace)

    return distances[index_s1 - 1][index_s2 - 1]

def get_random_string():
    length = random.randrange(1, 10)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x', 'y','z']

    string = ""
    for i in range(length):
        string += random.choice(letters)
    return string

s1 =  "abc"#get_random_string()
s2 = "fgh" #get_random_string()
distances = [[-1 for j in range(len(s2))] for i in range(len(s1))]
print(len(s1))
count = 0
distances_mem_with_index1(s1, s2, len(s1), len(s2), distances, count)
print(count)