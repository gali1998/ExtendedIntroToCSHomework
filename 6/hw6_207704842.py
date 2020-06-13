# Skeleton file for HW6 - Spring 2019/20 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).


############
# QUESTION 1
############

class ImprovedGenerator:
    def __init__(self, g):
        """
            fill-in your code below here according to the instructions
        """
        self.gen = g
        self.next_value = None
        self.does_have_next = False
        self.update_fields()

    def update_fields(self):
        try:
            n = next(self.gen)

            self.does_have_next = True
            self.next_value = n
        except:
            self.does_have_next = False
            self.next_value = None


    def has_next(self):
        """
            fill-in your code below here according to the instructions
        """
        return self.does_have_next

    def peek(self):
        """
            fill-in your code below here according to the instructions
        """
        return self.next_value

    def __iter__(self):
        return self
        # yield next(self)

    def __next__(self):
        """
            fill-in your code below here according to the instructions
        """
        if self.has_next() == True:
            result = self.next_value
            self.update_fields()

            return  result
        else:
            raise StopIteration

    def product(self, other):
        """
            fill-in your code below here according to the instructions
        """
        def couple_generator(g2):
            while True:
                yield (self.next_value, next(g2))
                self.__next__()

        g = couple_generator(other)
        return ImprovedGenerator(g)

############
# QUESTION 3
############
def maxmatch(T, p, triple_dict, w=2**12-1, max_length=2**5-1):
    """ finds a maximum match of length k<=2**5-1 in a w long window, T[p:p+k] with T[p-m:p-m+k].
        Returns m (offset) and k (match length) """

    assert isinstance(T,str)
    n = len(T)
    maxmatch = 0
    offset = 0
    if p + 3 > len(T) or T[p:p+3] not in triple_dict:
        return offset, maxmatch
    """
        fill-in your code below here according to the instructions
    """
    return offset, maxmatch


def LZW_compress(text, w=2**12-1, max_length=2**5-1):
    """LZW compression of an ascii text. Produces a list comprising of either ascii characters
       or pairs [m,k] where m is an offset and k>=3 is a match (both are non negative integers) """
    result = []
    n = len(text)
    p = 0
    triple_dict = {}

    while p<n:
        m,k = maxmatch(text, p, triple_dict, w, max_length)
        """
            fill-in your code below here according to the instructions
        """
    return result  # produces a list composed of chars and pairs

def add_triple_to_dict(text, p, triple_dict):
    """ Adds to the dictionary mapping from a key T[p:p+2] to a new
        integer in a list p."""
    if p+3 > len(text): return
    triple = text[p:p+3]
    if triple in triple_dict:
        triple_dict[triple].append(p)
    else:
        triple_dict[triple] = [p]



############
# QUESTION 6
############

###### CODE FROM LECTURE - DO NOT CHANGE ######
def fingerprint(text, basis=2 ** 16, r=2 ** 32 - 3):
    """ used to compute karp-rabin fingerprint of the pattern
        employs Horner method (modulo r) """
    partial_sum = 0
    for ch in text:
        partial_sum = (partial_sum * basis + ord(ch)) % r
    return partial_sum


def text_fingerprint(text, m, basis=2 ** 16, r=2 ** 32 - 3):
    """ computes karp-rabin fingerprint of the text """
    f = []
    b_power = pow(basis, m - 1, r)
    list.append(f, fingerprint(text[0:m], basis, r))
    # f[0] equals first text fingerprint
    for s in range(1, len(text) - m + 1):
        new_fingerprint = ((f[s - 1] - ord(text[s - 1]) * b_power) * basis + ord(text[s + m - 1])) % r
        # compute f[s], based on f[s-1]
        list.append(f, new_fingerprint)  # append f[s] to existing f
    return f
##############################################


def is_rotated_1(s, t, basis=2 ** 16, r=2 ** 32 - 3):
    """
    fill-in your code below here according to the instructions
    """
    index_s = 0
    index_t = len(t) - index_s

    for i in range(len(s)):
        beginning_s = s[0:index_s]
        ending_t = t[index_t:len(t)]

        beginnin_t = t[0:index_t]
        ending_s = s[index_s:len(s)]

        if (fingerprint(beginning_s, basis, r) == fingerprint(ending_t, basis, r)) and (fingerprint(ending_s, basis, r) == fingerprint(beginnin_t, basis, r)):
            return True

        index_s += 1
        index_t -= 1

    return False


def is_rotated_2(s, t):
    """
    fill-in your code below here according to the instructions
    """

    for m in range(len(s), 1, -1):
        fingerprints_beginnings_of_s = text_fingerprint(s, m)
        fingerprints_endings_of_t = text_fingerprint(t,m)

        m2 = len(t) - m
        fingerprints_ending_of_s = text_fingerprint(s, m2)
        fingerprints_beginnings_of_t = text_fingerprint(t, m2)

        if (fingerprints_beginnings_of_s[0] == fingerprints_endings_of_t[len(fingerprints_endings_of_t) - 1]) and (fingerprints_beginnings_of_t[0] == fingerprints_ending_of_s[len(fingerprints_ending_of_s) - 1]):
            return True
    return False


############
# QUESTION 7
############

from matrix import Matrix

# (1)
def had(n):
    mat = Matrix(pow(2,n), pow(2,n))
    """
        fill-in your code below here according to the instructions
    """
    return mat


# (2)
def disj(n):
    mat = Matrix(pow(2,n), pow(2,n))
    """
         fill-in your code below here according to the instructions
    """
    return mat

# (3)
def id_image():
    """
         fill-in your code below here according to the instructions
         use Matrix.load() to load the images
    """

########
# Tester
########

def test():

    # Question 1

    g = (i for i in range(5))
    g2 = ImprovedGenerator(g)
    for i in range(5):
        if g2.peek() != i:
            print("error in peek")

        if (i != 4 and (not g2.has_next())) or (i == 4 and g2.has_next()):
            print("error in has_next")

        if next(g2) != i:
            print("error in next")

    try:
        next(g2)
        print("should throw stopiteration")
    except StopIteration:
        print("raises StopIteration as should")
    except:
        print("not the correct exception")

    g1 = (i for i in range(3))
    g2 = (i for i in range(3))

    g3 = ImprovedGenerator(g1)
    g4 = ImprovedGenerator(g2)
    g5 = g3.product(g4)

    for i in range(3):
        if next(g5) != {i,i}:
            print("error in product")

    # Question 3

    # first convert to tuple to make easy comparison
    compressed = tuple([el if isinstance(el, str) else tuple(el) for el in LZW_compress("abcdabc")])
    if compressed != ('a', 'b', 'c', 'd', (4, 3)):
        print("error in LZW_compress")

    # Question 6
    for func in [is_rotated_1, is_rotated_2]:
        if func("amirrub", "rubamir") != True or \
                func("amirrub", "bennych") != False or \
                func("amirrub", "ubamirr") != True:
            print("error in", func.__name__)

    # Question 7

    # (1)
    had1 = Matrix(2, 2)
    had1[1, 1] = 1
    if had(1)!=had1:
        print("error in had")

    # (2)
    disj1 = Matrix(2, 2, 1)
    disj1[1, 1] = 0
    if disj(1) != disj1:
        print("error in disj")