# Skeleton file for HW2 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw2_ID.py).

import math

############
# QUESTION 1
############

# 1a
def sum_divisors(n):
    if n == 1:
        return 0

    upperBound = math.floor(n ** 0.5) + 1
    sum = 1

    for i in range(2, upperBound):
        if n % i == 0:
            sum += i

            if i ** 2 != n:
                sum += n // i

    return sum


# 1b
def isOpener(char):
    return char in ['(', '{', '[', '<']


def arePaired(opener, closer):
    openers = ['(', '{', '[', '<']
    closers = [')', '}', ']', '>']

    return openers.index(opener) == closers.index(closer)

def legal_par(st):
    openers = []

    for char in st:
        if isOpener(char):
            openers.append(char)
        else:
            openersLength = len(openers)
            if openersLength == 0 or arePaired(openers.pop(openersLength-1), char) == False:
                return False

    return len(openers) == 0

# 1c

def spiral_sum(k):
    sum = 1

    for n in range(3, k + 2, 2):
        sum = sum + ((4 * (n*n)) - 6*(n-1))

    return sum

############
# QUESTION 2
############

# 2b
def power_new(a, b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[::-1]
    for bit in reverse_b_bin:
        if bit == "1":
            result = result * a
        a = a * a
    return result

# 2c
def modpower_new(a, b, c):
    """ computes a**b mod c using iterated squaring
        assumes b is nonnegative integer  """
    print("a=" + str(a) + " b= " + str(b) + " c= " + str(c))
    result = 1 # a**0
    while b > 0:
        if b % 3 == 0:
            result = (result) % c
            a = (a * a * a) % c
        if b % 3 == 1:
            result = (result*a) % c
            a = (a*a*a) % c
        if b % 3 == 2:
            result = (result*a*a) % c
            a = (a*a*a) % c
        b = b // 3
    return result

print(str(modpower_new(3, 4, 5)),  str(pow(3, 4, 5)))
print(modpower_new(5, 4, 2) != pow(5, 4, 2))

############
# QUESTION 3
############

# 3a
def inc(binary):
    temp = binary
    result = ""

    while temp != "":
        if temp[len(temp) - 1] == "1":
            result = "0" + result

        else:
            return temp[0: len(temp) -1] + "1" + result

        temp = temp[0: len(temp) -1]

    return "1" + "0" * len(binary)

# 3b
def dec(binary):
    temp = binary
    result = ""

    if binary == "1":
        return "0"

    while temp != "1":
        if temp[len(temp) - 1] == "0":
            result = "1" + result
        else:
            return temp[0: len(temp) -1] + "0" + result

        temp = temp[0: len(temp) -1]

    return "1" * (len(binary) - 1)

# 3c
def sub(bin1, bin2):
    tempBin1 = bin1
    tempBin2 = bin2
    result = ""

    if bin2 == bin1:
        return "0"

    while tempBin2 != "" and tempBin1 != tempBin2:
        digit = tempBin2[len(tempBin2) - 1]

        if digit == "1":
            tempBin1 = dec(tempBin1)

        result = tempBin1[len(tempBin1) - 1] + result

        tempBin2 = tempBin2[0: len(tempBin2) - 1]
        tempBin1 = tempBin1[0: len(tempBin1) - 1]

    if tempBin2 == tempBin1:
        return result

    return tempBin1 + result

# 3d
def leq(bin1, bin2):
    if len(bin1) > len(bin2):
        return False
    if len(bin1) < len(bin2):
        return True
    # if this happens bin1 and bin2 have the same number of bits
    for i in range(len(bin1)):
        if bin1[i] == "1" and bin2[i] == "0":
            return False

        if bin1[i] == "0" and bin2[i] == "1":
            return True

    return True

# 3e
def div(bin1, bin2):
    temp = bin1
    result = "0"

    while(leq(bin2, temp)):
        result = inc(result)
        temp = sub(temp, bin2)

    return result


############
# QUESTION 4
############

# 4a
def getSubList(lst, start, end):
    return lst[start:end]

def has_repeat1(s, k):
    upperIndex = len(s) - k + 1

    substringSet = {getSubList(s, i, i + k) for i in range(upperIndex)}

    return len(substringSet) < upperIndex

# 4b
def has_repeat2(s, k):
    upperIndex = len(s) - k + 1

    for i in range(upperIndex):
        substring = s[i: i + k]

        if substring in s[i + 1: len(s)]:
            return True

    return False

############
# QUESTION 5
############
def getReadingString(strnum):
    currentNum = strnum[0]
    count = 0
    result = ""

    for char in strnum:
        if char == currentNum:
            count += 1
        else:
            result = result + (str(count) + str(currentNum))
            count = 1
            currentNum = char

    result = result + str(count) + str(currentNum)
    return result

def reading(n):
    result = "1"
    for i in range(1, n):
        temp = getReadingString(result)
        result = temp

    return result

############
# QUESTION 6
############
def max_div_seq(n, k):
    max = 0
    count = 0
    temp = n

    while temp > 0:
        digit = temp % 10

        if digit % k == 0:
            count += 1
        else:
            count = 0

        if max < count:
            max = count

        temp = temp // 10

    return max


########
# Tester
########

def test():
    if sum_divisors(4) != 3 or \
            sum_divisors(220) != 284:
        print("error in sum_divisors")

    if not legal_par("<<>>") or legal_par("<{>}"):
        print("error in legal_par")
    if not legal_par("<<{}<>()[<>]>>") or legal_par("{{{]}}"):
        print("error in legal_par")

    if spiral_sum(3) != 25 or spiral_sum(5) != 101:
        print("error in spiral_sum")

    if power_new(2, 3) != 8:
        print("error in power_new()")

    if modpower_new(3, 4, 5) != pow(3, 4, 5) or \
            modpower_new(5, 4, 2) != pow(5, 4, 2):
        print("error in modpower_new()")

    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("error in inc()")

    if dec("1") != "0" or \
            dec("10") != "1" or \
            dec("110") != "101" or \
            dec("1000") != "111" or \
            dec(dec("1001")) != "111":
        print("error in dec()")

    if sub("0", "0") != "0" or \
            sub("1000", "0") != "1000" or \
            sub("1000", "1000") != "0" or \
            sub("1000", "1") != "111" or \
            sub("101", "100") != "1":
        print("error in sub()")

    if leq("100", "11") or not leq("11", "100"):
        print("error in leq")
    if div("1010", "10") != "101" or div("11001", "100") != "110":
        print("error in div")

    if not has_repeat1("ababa", 3) or \
            has_repeat1("ababa", 4) or \
            not has_repeat1("aba", 1):
        print("error in has_repeat1()")

    if not has_repeat2("ababa", 3) or \
            has_repeat2("ababa", 4) or \
            not has_repeat2("aba", 1):
        print("error in has_repeat2()")

    if [reading(i) for i in range(1, 6)] != ['1', '11', '21', '1211', '111221']:
        print("error in reading")

    if max_div_seq(23300247524689, 2) != 4:
        print("error in max_div_seq()")
    if max_div_seq(1357, 2) != 0:
        print("error in max_div_seq()")