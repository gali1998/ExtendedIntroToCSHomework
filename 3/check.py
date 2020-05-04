import random
import time
from skeleton import  *


def something(n, p):
    matrix = [[0 for j in range(n)] for j in range(n)] # O(n^2)
    weights = [p*100] * n # O(n)
    indexes = [i for i in range(0, n)] # O(n)

    for row in matrix:
        ones = random.choices(indexes, weights)

        for i in ones:
            row[i] = 1
    return matrix



"""for i in range(10):
    for n in [125, 250, 500, 1000, 2000, 10000]:
        print("===== " + str(n) + "=====")
        for p in [0.3, 0.5, 0.7]:
            count_0 = 0
            count_1 = 0

            matrix = something(n, p)

            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 1:
                        count_1 += 1
                    else:
                        count_0 += 1

            print("expected: " + str(p))
            print("actual: " + str(count_1 / (count_0 + count_1)))"""
ns = []
for i in range(10):
    n = 2
    t = 0

    while t < 60:

        t0 = time.perf_counter()
        cover_time(return_graph(n))

        t1 = time.perf_counter()

        t = t1-t0
        n += 1
    print(n)
    ns.append(n)
print("finished" + str(sum(ns)/ 10))




"""for n in [125, 250, 500, 1000, 2000]:
    print("===== " + str(n) + "=====")
    for p in [0.3, 0.5, 0.7]:
        count_1 = time.perf_counter()
        matrix = random_graph(n, p)
        cover_time(matrix)

        count_0 = time.perf_counter()
        print(count_0 - count_1)
        if count_0 - count_1 >= 60:
            print("problem")
        else:
            print("ok")"""
