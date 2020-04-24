import random
import string
from hw2_207704842 import *

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def chooseRandomSubstring():
    n = random.randrange(1, 100)

    return randomString(n)

def getSumOfDivisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum

def compareRandomDiv():
    n2 = random.randrange(0, 100000)
    n1 = random.randrange(0, 100000)

    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]

    expected = bin((n1 // n2))[2:]

    return expected == div(bin1, bin2)

def compareRandomDivSmaller():
    n2 = random.randrange(0, 100000)
    n1 = random.randrange(n2, n2 + 100000)

    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]

    expected = bin((n1 // n2))[2:]

    return expected == div(bin1, bin2)

def compareRandomLeq():
    n2 = random.randrange(0, 100000)
    n1 = random.randrange(0, 100000)

    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]

    return ((n1 <= n2) == leq(bin1, bin2))

def compareRandomInc():
    n = random.randrange(0, 100000)
    binary = bin(n)[2:]
    expected = bin(n+1)[2:]
    actual = inc(binary)

    return expected == actual

def compareRandomSub():
    n2 = random.randrange(1, 100000)
    n1 = random.randrange(n2, n2 + 100000)

    bin1 = bin(n1)[2:]
    bin2 = bin(n2)[2:]
    expected = bin(n1-n2)[2:]
    actual = sub(bin1, bin2)

    return expected == actual

def compareRandomDec():
    n = random.randrange(1, 100000)
    binary = bin(n)[2:]
    expected = bin(n-1)[2:]
    actual = dec(binary)

    return expected == actual

def compareRandomSumDivisors():
    n = random.randrange(1, 100000)
    expected = getSumOfDivisors(n)
    actual = sum_divisors(n)

    return expected == actual