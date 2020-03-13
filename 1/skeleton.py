#Skeleton file for HW1 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw1_ID.py).

from primes_lst import *  #loading the list of primes into a variable named primes

#Question 3
def max_word_len(filename):
    inFile = open(filename, "r")
    outFile = open("output.txt", "w")

    for line in inFile:
        line = line.replace("\n", "")
        maxLetters = 0

        words = line.split(" ")

        for word in words:
            if len(word) > maxLetters:
                maxLetters = len(word)

        outFile.write(str(maxLetters)+"\n")

#**************************************************************
#Question 5
def k_boom(start, end, k):
    currentNumber = start;
    returnValue = ""

    while currentNumber <= end:
        dividedBySeven = currentNumber % 7 == 0
        numberOfSevens = str(currentNumber).count("7")

        if dividedBySeven:
            if (numberOfSevens == 0):
                returnValue += "boom! "
            else:
                returnValue += "bada-boom! "
                
        elif numberOfSevens > 0:
            booms = "boom-" * numberOfSevens
            booms = booms[:-1]
            booms += "!"
        
            returnValue += (booms + " ")
        else:
            returnValue += (str(currentNumber)+" ")

        currentNumber += 1

    returnValue = returnValue[:-1]
    
    return returnValue

#**************************************************************
#Question 6

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
    areAllGoldbach = True
    
    for evenNumber in range(4, limit, 2):
        if (check_goldbach_for_num(evenNumber, primes_lst) == False):
            areAllGoldbach = False
            break

    return areAllGoldbach
        

# 6c
def check_goldbach_for_num_stats(n, primes_lst):
    pass #replace this with your code


########
# Tester
########

def test():
    #testing Q5
    s = k_boom(797, 802, 7)
    if s != 'boom-boom! bada-boom! boom! 800 801 802':
        print("error in k_boom()")
    #testing Q6
    if not check_goldbach_for_num(10, [2, 3, 5, 7]):
        print("error in check_goldbach_for_num()")

    if check_goldbach_for_num(10, [2, 3]):
        print("error in check_goldbach_for_num()")

    if not check_goldbach_for_range(20, [2, 3, 5, 7, 11]):
        print("error in check_goldbach_for_range()")

    if check_goldbach_for_range(21, [2, 3, 5, 7, 11]):
        print("error in check_goldbach_for_range()")
        
    if check_goldbach_for_num_stats(20, primes) != 2:
        print("error in check_goldbach_for_num_stats()")

    if check_goldbach_for_num_stats(10, primes) != 2:
        print("error in check_goldbach_for_num_stats()")

   
