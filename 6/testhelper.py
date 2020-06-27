import random

import string

def get_string_with_one_different_char(s):
    n = random.randrange(0, len(s))
    letters = string.ascii_lowercase

    c = s[n]
    k = c
    while(k == c):
        k = random.choice(letters)

    result = ""
    for i in range(len(s)):
        if i != n:
            result += s[i]
        else:
            result += k
    return result
def rotate(strg, n):
    return strg[n:] + strg[:n]
def randomString():
    stringLength = 10#random.randrange(100, 1000)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def maxmatch1(T, p, W=2**12-1, max_length=2**5-1):
    """ finds a maximum match of length k<=2**5-1 in a
        W long window, T[p:p+k] with T[p-m:p-m+k].
        Returns m (offset) and k (match length) """
    assert isinstance(T,str)
    n = len(T)
    maxmatch = 0
    offset = 0
    for m in range(1, 1+min(p, W)):
        k = 0
        while k < min(n-p, max_length) and T[p-m+k] == T[p+k]:
            k+=1  # at this point, T[p-m:p-m+k]==T[p:p+k]
        if k > maxmatch:
            maxmatch = k
            offset = m
    return offset, maxmatch # returned offset is smallest one (closest to p)
                            # among all max matches (m starts at 1)



def LZW_compress1(text, W=2**12-1, max_length=2**5-1):
    """LZW compression of an ascii text. Produces
       a list comprising of either ascii characters
       or pairs [m,k] where m is an offset and
       k>=3 is a match (both are non negative integers) """
    result = []
    n = len(text)
    p = 0
    while p<n:
        m,k = maxmatch1(text, p, W, max_length)
        if k<3:
            result.append(text[p]) #  a single char
            p+=1
        else:
            result.append([m,k])   # two or more chars in match
            p+=k
    return result  # produces a list composed of chars and pairs

