import random
import time
from skeleton import *
def checm_times():
    t0 = time.perf_counter()
    input1 = "1"*10 + "0"*20+ "1"*20
    input2 = input1[0:29] + "11"*21
    print(inc("1"*100))

    t1 = time.perf_counter()

    print((t1-t0) < 1)

checm_times()

print(spiral_sum(11))