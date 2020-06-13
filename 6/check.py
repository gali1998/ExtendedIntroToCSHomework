from hw6_207704842 import *

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

imp = ImprovedGenerator(countup_finite)

g = (i for i in range(10))
g2 = (i for i in range(10, 20))
X = ImprovedGenerator(g)
Y = ImprovedGenerator(g2)
Z = X.product(Y)
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

s = "introtocs"
t = "sintrotoc"
print("%%%%%%%%%%%%%%%%%%%%%%%%%")
print(is_rotated_2(s,t))
