from hw6_207704842 import *
from testhelper import *

# infinite generator

def countup_infinite():
    i = 0
    while True:
        yield i
        i += 1

def countup_finite():
    i = 0
    while(i < 4):
        yield i
        i += 1


'''print(Z.peek())
print(Z.has_next())
print(next(Z))
print(next(Z))
print(Z.peek())
print(Z.has_next())
print(next(Z))'''
'''try:
    print(next(imp))
    print(imp.has_next())
    print(next(imp))
    print(next(imp))
    print(next(imp))
    print(imp.has_next())
    print(next(imp))
except Exception as e:
    print(type(e))'''

s = "amirgil"
t = "amirrub"
'''print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print(is_rotated_2(s,t))
m = Matrix(2,3)
m[1,1] = 1
s,d = m.dim()
print(m)
print(s)
print(d)'''

def join_v(mat1, mat2):
    """ joins two matrices, vertically with some separation """
    n1,m1 = mat1.dim()
    n2,m2 = mat2.dim()
    n = n1+n2+10 #+10 to separate between the images
    m = max(m1,m2)
    new = Matrix(n, m, val=255)  # fill new matrix with white pixels

    new[:n1,:m1] = mat1
    new[n1+10:n,:m2] = mat2

    return new

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


'''m2 = Matrix.load("2.bitmap")
m0 = Matrix.load("0.bitmap")
m7 = Matrix.load("7.bitmap")
m4 = Matrix.load("4.bitmap")
m8 = Matrix.load("8.bitmap")

m = join_h(m2, m0)
m = join_h(m, m7)
m = join_h(m, m7)
m = join_h(m, m0)
m = join_h(m, m4)
m = join_h(m, m8)
m = join_h(m, m4)
m = join_h(m, m2)
k = Matrix(20, 10, 255)
f = Matrix(1,10)
print(k.dim())
m = join_h(k, m)
m = join_h(m, k)
m = join_v(m ,f)
print(m.dim())
#id_image().display()'''
'''def maxmatch(T, p, triple_dict, w=2*12-1, max_length=2*5-1):
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
    # Get the matching triplet indexes
    triple_list = triple_dict[T[p:p+3]]
    for k in range(max_length, 2, -1):
        for i in range(len(triple_list)-1, -1, -1):
            triple_index = triple_list[i]
            if triple_index < n-w:
                break
            if T[p:p+k] == T[triple_index: triple_index+k]:
                offset = p - triple_index
                maxmatch = k
                break
        if maxmatch != 0:
            break
    return offset, maxmatch


def LZW_compress(text, w=2*12-1, max_length=2*5-1):
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
        if k == 0:
            result.append(text[p])
        else:
            result.append((m,k))
        add_triple_to_dict(text, p, triple_dict)
        if k != 0:
            p += k
        else:
            p += 1
    return result  # produces a list composed of chars and pairs'''


for i in range(100):
    s = randomString()
    n = random.randrange(0, len(s))
    t1 = (rotate(s, 5))
    t2 = get_string_with_one_different_char(s)
    t3 = t1 + "a"
    #print(s)

    #print(is_rotated_1(s, t1))
    if is_rotated_2(s, t1) == False:
        print("false")
#print(is_rotated_1(s, t2))
#print(is_rotated_2(s, t2))
#print(is_rotated_2(s, t3))