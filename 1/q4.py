import time
"""
def func(e):
    return e["time"]
times1 = 1
times0 = 100000 - 1
strnum = "1" * times1 + "0" * times0
num = int(strnum)

##################################################3
t0 = time.perf_counter()
m = num
cnt = 0

while m > 0:
    if m % 10 == 0:
        cnt = cnt + 1

    m = m // 10

t1 = time.perf_counter()
print(num, "has ", cnt, " zeros")
solution1time = t1-t0
print("Running time: ", solution1time, " sec")
####################################################
t0 = time.perf_counter()
cnt = 0
snum = str(num)

for digit in snum:
    if digit == "0":
        cnt = cnt + 1
t1 = time.perf_counter()
print(num, "has ", cnt, " zeros")
solution2time = t1-t0
print("Running time: ", t1-t0, " sec")
######################################################
t0 = time.perf_counter()
cnt = str.count(str(num), "0")

t1 = time.perf_counter()
print(num, "has ", cnt, " zeros")
solution3time = t1-t0
print("Running time: ", t1-t0, " sec")
#######################################################

lst = [{"name": "solution 1", "time": solution1time},{"name": "solution 2", "time": solution2time}, {"name": "solution 3", "time": solution3time}]
lst.sort(key=func)
print(lst)

t0 = time.perf_counter()
num = 1
cnt = 0
for i in range(num):
    cnt = cnt + 1

t1 = time.perf_counter()
print(num, "has ", cnt, " zeros")
solution3time = t1-t0
print("Running time: ", t1-t0, " sec")

"""

from hw1_207704842 import *
from primes_lst import *
t0 = time.perf_counter()
check_goldbach_for_num_stats(10000, primes)
t1 = time.perf_counter()
print("Goldbach Running time: ", t1-t0, " sec")


