from hw6_207704842 import *

'''compressed = tuple([el if isinstance(el, str) else tuple(el) for el in LZW_compress("abcdabc")])
print(compressed)

m = id_image()
m.display()
s = "introtocs"
t = "sintrotoc"
print(is_rotated_1(s,t))
'''


id = id_image()
h  = had(8)
dis = disj(8)

x = join(h, dis, id, direction="h")