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
def maxmatch(T, p, triple_dict, w=2 ** 12 - 1, max_length=2 ** 5 - 1):
    """ finds a maximum match of length k<=2**5-1 in a w long window, T[p:p+k] with T[p-m:p-m+k].
           Returns m (offset) and k (match length) """

    assert isinstance(T, str)
    n = len(T)
    maxmatch = 0
    offset = 0
    if p + 3 > len(T) or T[p:p + 3] not in triple_dict:
        return offset, maxmatch
    """
        fill-in your code below here according to the instructions
    """

    match_indexes = triple_dict[T[p:p+3]]

    for i in range(len(match_indexes) - 1, -1, -1):

        m = p - match_indexes[i]
        print(m)
        if m >= w:
            break
        k = 0
        while k < min(n - p, max_length) and T[p-m+k] == T[p + k]:
            print(T[p-m+k])
            print(T[p + k])

            k += 1
        if maxmatch < k:
            maxmatch = k
            offset = m
    print(triple_dict)
    return offset, maxmatch


def LZW_compress(text, w=2 ** 12 - 1, max_length=2 ** 5 - 1):
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
        if k < 3:
            result.append(text[p])
            add_triple_to_dict(text, p, triple_dict)
            p+=1
        else:
            result.append([m,k])
            for i in range(k):
                add_triple_to_dict(text, p+i, triple_dict)
            p+=k
    return result  # produces a list composed of chars and pairs


def add_triple_to_dict(text, p, triple_dict):
    """ Adds to the dictionary mapping from a key T[p:p+2] to a new
        integer in a list p."""
    if p + 3 > len(text): return
    triple = text[p:p + 3]
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
    if len(t) != len(s):
        return False
    if s == t:
        return True
    fingerprint1 = fingerprint(s, basis, r)
    fingerprint2 = fingerprint(t, basis, r)
    b_power = pow(basis, len(t) - 1, r)

    for i in range(len(t)):
        if fingerprint1 == fingerprint2:
            return True
        ord_of_letter = ord(t[i])
        fingerprint2 = ((fingerprint2 - (ord_of_letter * b_power))*basis + ord_of_letter) % r
    return False


def is_rotated_2(s, t):
    """
    fill-in your code below here according to the instructions
    """
    if len(t) != len(s):
        return False
    if len(t) == 0:
        return True
    for m in range(len(s), 0, -1):
        fingerprint_beginning_of_s = text_fingerprint(s, m)[0]
        fingerprints_endings_of_t = text_fingerprint(t, m)
        fingerprint_ending_of_t = fingerprints_endings_of_t[len(fingerprints_endings_of_t) - 1]

        m2 = len(t) - m
        fingerprints_ending_of_s = text_fingerprint(s, m2)
        fingerprint_ending_of_s = fingerprints_ending_of_s[len(fingerprints_ending_of_s) - 1]
        fingerprint_beginning_of_t = text_fingerprint(t, m2)[0]

        if (fingerprint_beginning_of_s == fingerprint_ending_of_t) and (
                fingerprint_beginning_of_t == fingerprint_ending_of_s):
            return True
    return False

#print(is_rotated_2("zdwtffnohb", "dwtffnohbz"))
############
# QUESTION 7
############

from matrix import Matrix

def is_in_inverse(n, i, j):
    size_of_block = pow(2, n-1)

    return (i >= size_of_block) and (j >= size_of_block)

def had_local(n, i, j):
    if n == 0:
        return 0
    size = pow(2, n-1)

    if is_in_inverse(n, i, j):
        return 1 - had_local(n-1, i - size, j - size)
    if i >= size:
        i = i - size

    if j >= size:
        j = j - size

    return had_local(n-1, i, j)


# (1)
def had(n):
    mat = Matrix(pow(2, n), pow(2, n))
    rows, columns = mat.dim()

    for i in range(rows):
        for j in range(rows):
            mat[i, j] = had_local(rows, i, j)
    return mat


# (2)

def get_row(mat, i):
    n, m = mat.dim()
    result = []

    for j in range(m):
        result.append(mat[i, j])


    return result


def get_column(mat, i):
    n, m = mat.dim()
    result = []

    for j in range(m):
        result.append(mat[j, i])


    return result
def getS(v):
    result = []

    for i in range(len(v)):
        if v[i] == 1:
            result.append(i)
    return result
def is_union_empty(g1, g2):
    for i in range(len(g1)):
        if g1[i] in g2:
            return False
    return True

def get_binary_matrix(n):
    m = Matrix(n, n)

    for i in range(n):
        rep = format(i, "0"+str(n)+"b")

        for j in range(n):
            if rep[j] == "0":
                m[i,j] = 0
            else:
                m[i,j] = 1
    return m

def disj(n):
    mat = Matrix(pow(2, n), pow(2, n), 1)
    l = pow(2,n)
    """
         fill-in your code below here according to the instructions
    """
    for i in range(l):
        for j in range(l):
            row = format(i, "b")
            col = format(j, "b")
            len_row = len(row)
            len_col = len(col)
            index_row = len_row - 1
            index_col = len_col - 1

            for k in range(min(len_row, len_col)):
                if row[index_row] == col[index_col] and col[index_col] == "1":
                    mat[i,j] = 0
                index_col -= 1
                index_row -= 1

    return mat

def join_h(mat1, mat2):
    """ joins two matrices, side by side with some separation """
    n1,m1 = mat1.dim()
    n2,m2 = mat2.dim()
    m = m1+m2+10 #+10 to separate between the images
    n = max(n1,n2)
    new = Matrix(n, m, val=255)  # fill new matrix with white pixels

    new[:n1,:m1] = mat1
    new[:n2,m1+10:m] = mat2

    return new
def join_v(mat1, mat2):
    """ joins two matrices, vertically with some separation """
    n1,m1 = mat1.dim()
    n2,m2 = mat2.dim()
    n = n1+n2 #+10 to separate between the images
    m = max(m1,m2)
    new = Matrix(n, m, val=255)  # fill new matrix with white pixels

    new[:n1,:m1] = mat1
    new[n1:n,:m2] = mat2

    return new
def join(*mats, direction):
    ''' *mats enables a variable number of parameters.
        direction is either 'h' or 'v', for horizontal or vertical join, respectively '''
    func = join_v if direction == 'v' else join_h
    res = mats[0] #first matrix parameter
    for mat in mats[1:]:
        res = func(res, mat)
    return res
# (3)

def get_images():
    m2 = Matrix.load("2.bitmap")
    m0 = Matrix.load("0.bitmap")
    m7 = Matrix.load("7.bitmap")
    m4 = Matrix.load("4.bitmap")
    m8 = Matrix.load("8.bitmap")

    result = {"2": m2, "0": m0, "7": m7, "4": m4, "8": m8}
    return result

def id_image():
    """
         fill-in your code below here according to the instructions
         use Matrix.load() to load the images
    """
    # load images
    numbers = get_images()

    m = join(numbers["2"],numbers["0"],numbers["2"],numbers["7"],numbers["7"],numbers["0"],numbers["4"],numbers["8"],numbers["4"],numbers["2"], direction='h')

    # pad with white pixels so the matrix will be 30x300
    k = Matrix(10,  300, 255)
    m = join_v(m, k)

    return m


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

        if next(g2) != i:
            print("error in next")

        if (i != 4 and (not g2.has_next())) or (i == 4 and g2.has_next()):
            print("error in has_next")

    try:
        next(g2)
        print("should throw stopiteration")
    except StopIteration:
        print("GOOD: raises StopIteration as should")
    except:
        print("not the correct exception")

    g1 = (i for i in range(3))
    g2 = (i for i in range(3))

    g3 = ImprovedGenerator(g1)
    g4 = ImprovedGenerator(g2)
    g5 = g3.product(g4)

    for i in range(3):
        if next(g5) != (i, i):
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
    if had(1) != had1:
        print("error in had")

    # (2)
    disj1 = Matrix(2, 2, 1)
    disj1[1, 1] = 0
    if disj(1) != disj1:
        print("error in disj")