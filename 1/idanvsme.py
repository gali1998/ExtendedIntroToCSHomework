from primes_lst import *  #loading the list of primes into a variable named primes

def max_word_len(filename):
    inFile = open(filename, "r")
    outFile = open("output1.txt", "w")

    for line in inFile:
        line = line.replace("\n", "")
        maxLetters = 0

        words = line.split(" ")

        for word in words:
            if len(word) > maxLetters:
                maxLetters = len(word)

        outFile.write(str(maxLetters) + "\n")
    inFile.close()
    outFile.close()


# **************************************************************
# Question 5
def k_boom(start, end, k):
    currentNumber = start
    returnValue = ""

    while currentNumber <= end:
        dividedByk = currentNumber % k == 0
        numberOfKs = str(currentNumber).count(str(k))

        if dividedByk:
            if (numberOfKs == 0):
                returnValue += "boom! "
            else:
                returnValue += "bada-boom! "

        elif numberOfKs > 0:
            booms = "boom-" * numberOfKs
            booms = booms[:-1]
            booms += "!"

            returnValue += (booms + " ")
        else:
            returnValue += (str(currentNumber) + " ")

        currentNumber += 1

    returnValue = returnValue[:-1]

    return returnValue


# **************************************************************
# Question 6

# 6a
def check_goldbach_for_num(n, primes_lst):
    isGoldbach = False

    for firstPrimeNumber in primes_lst:
        for secondPrimeNumber in primes_lst:
            if n == firstPrimeNumber + secondPrimeNumber:
                isGoldbach = True
        if isGoldbach:
            break

    return isGoldbach


# 6b
def check_goldbach_for_range(limit, primes_lst):
    if limit == 4:
        return True

    areAllGoldbach = True

    for evenNumber in range(4, limit, 2):
        if (check_goldbach_for_num(evenNumber, primes_lst) == False):
            areAllGoldbach = False
            break

    return areAllGoldbach


# 6c
def check_goldbach_for_num_stats(n, primes_lst):
    pairCount = 0
    pairs = []

    for firstPrime in primes_lst:
        for secondPrime in primes_lst:
            if (n == firstPrime + secondPrime):
                str1 = str(firstPrime) + "," + str(secondPrime)
                str2 = str(secondPrime) + "," + str(firstPrime)

                if (list.count(pairs, str1) == 0 and list.count(pairs, str2) == 0):
                    pairs.append(str1)
                    pairCount += 1
    return pairCount




# Question 3
def idan_max_word_len(filename):
    inFile = open(filename, "r")
    outFile = open("output2.txt", "w")
    for line in inFile:
        word_list = line.split()
        max_length_in_row = 0
        for word in word_list:
            word_len = len(word)
            if max_length_in_row < word_len:
                max_length_in_row = word_len
            if word.count('\n') > 0 or word.count(' '):
                print(word, len(word))
        outFile.write(str(max_length_in_row ) + '\n')

# **************************************************************
# Question 5
def idan_k_boom(start, end, k):
    str_result = ""
    for num in range(start, end + 1):
        num_of_k = str(num).count(str(k))
        if num%k == 0:
            if num_of_k > 0:
                str_result += "bada-boom!"
            else:
                str_result += "boom!"
        else:
            if num_of_k > 0:
                booms = ("boom-"*(num_of_k - 1)) + "boom!"
                str_result += booms
            else:
                str_result += str(num)
        if num < end:
            str_result += " "
    return str_result


# **************************************************************
# Question 6

# 6a
def idan_check_goldbach_for_num(n, primes_lst):
    primes_under_n = list(set(primes_lst) & set(range(n)))
    for i in primes_under_n:
        primes_under_i = list(set(primes_lst) & set(range(i + 1)))
        for k in primes_under_i:
            if i + k == n:
                return True
    return False

# 6b
def idan_check_goldbach_for_range(limit, primes_lst):
    for n in range(2, int((limit-1)/2) + 1):
        if not check_goldbach_for_num(2*n, primes_lst):
            return False
    return True


# 6c
def idan_check_goldbach_for_num_stats(n, primes_lst):
    primes_under_n = list(set(primes_lst) & set(range(n)))
    prime_couples_counter = 0
    for i in primes_under_n:
        primes_under_i = list(set(primes_lst) & set(range(i + 1)))
        for k in primes_under_i:
            if i + k == n:
                print(i, k)
                prime_couples_counter += 1
    return prime_couples_counter
