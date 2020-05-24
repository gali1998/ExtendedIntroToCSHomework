# Skeleton file for HW5 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw5_ID.py).


############
# QUESTION 1
############
class Permutation:
    def __init__(self, perm):
        self.perm = None
        def is_legal(lst):
            seen_list = [0 for i in range(len(lst))]

            for number in lst:
                if number < 0 or number > (len(lst) - 1) or seen_list[number] != 0:
                    return False
                seen_list[number] += 1

            return True

        if is_legal(perm):
            self.perm = perm

    def __getitem__(self, i):
        return self.perm[i]

    def compose(self, other):
        return Permutation([self[other[i]] for i in range(len(self.perm))])

    def inv(self):
        inv_perm = [-1 for i in range(len(self.perm))]

        for i in range(len(self.perm)):
            value = self[i]
            inv_perm[value] = i

        return Permutation(inv_perm)

    def __eq__(self, other):
        return self.perm == other.perm

    def __ne__(self, other):
        return self.perm != other.perm

    def order(self):
        n = len(self.perm)
        identity_perm = Permutation([i for i in range(n)])
        order = 1
        current_perm = self

        while(current_perm != identity_perm):
            current_perm = current_perm.compose(self)
            order += 1
        return order


# This function is not part of the class Permutation
def compose_list(lst):
   return compose_list_with_index(lst, 0)

def compose_list_with_index(lst, index):
    if index == len(lst) - 1:
        return lst[index]

    current = index
    return lst[current].compose(compose_list_with_index(lst, index + 1))


############
# QUESTION 2
############

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "|" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    def minimum(self):
        ''' return node with minimal key '''
        if self.root == None:
            return None
        node = self.root
        left = node.left
        while left != None:
            node = left
            left = node.left
        return node

    def depth(self):
        ''' return depth of tree, uses recursion'''

        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)

    def size(self):
        ''' return number of nodes in tree, uses recursion '''

        def size_rec(node):
            if node == None:
                return 0
            else:
                return 1 + size_rec(node.left) + size_rec(node.right)

        return size_rec(self.root)

    def max_sum(self):
        '''
        fill-in your code below here according to the instructions
        '''
        def max_sum_rec(node):
            if node == None:
                return 0
            left_sum = node.val + max_sum_rec(node.left)
            right_sum = node.val + max_sum_rec(node.right)

            return max(left_sum, right_sum)
        return max_sum_rec(self.root)

    def is_balanced(self):
        '''
        fill-in your code below here according to the instructions
        '''
        def get_depth(node):
            if node == None:
                return 0
            left = get_depth(node.left)
            right = get_depth(node.right)

            return max(left, right) + 1
        def is_balanced_node(node):
            if node == None:
                return True
            left = get_depth(node.left)
            right = get_depth(node.right)

            if abs(left - right) <= 1 and is_balanced_node(node.left) and is_balanced_node(node.right):
                return True
            return False

        return is_balanced_node(self.root)


    def diam(self):
        '''
        fill-in your code below here according to the instructions
        '''
        if self.root == None:
            return 0
        def max_distance(node):
            if node == None:
                return 0
            left = max_distance(node.left)
            right = max_distance(node.right)

            return 1 + max(left, right)

        def node_diam(node):
            if node == None:
                return 0
            left = max_distance(node.left)
            right = max_distance(node.right)

            return max(1 + left + right, node_diam(node.left), node_diam(node.right))

        return node_diam(self.root)


############
# QUESTION 3
############
def same_tree(lst1, lst2):
    length = len(lst1) # both lists are of the same size

    if length == 0:
        return True

    # if the roots are different the trees are different
    if lst1[0] != lst2[0]:
        return False

    lst1_left = []
    lst1_right = []
    lst2_left = []
    lst2_right = []

    # divide arrays into subtrees
    for i in range(1, length):
        if lst1[i] < lst1[0]:
            lst1_left.append(lst1[i])
        else:
            lst1_right.append((lst1[i]))

        if lst2[i] < lst2[0]:
            lst2_left.append(lst2[i])
        else:
            lst2_right.append((lst2[i]))
    return same_tree(lst1_right, lst2_right) and same_tree(lst1_left, lst2_left)


############
# QUESTION 4
############

class Node():

    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value) + "(" + str(id(self)) + ")"
    # This shows pointers as well for educational purposes


class DLList():

    def __init__(self, seq=None):
        self.head = None
        self.tail = None
        self.len = 0
        if seq != None:
            for item in seq:
                self.insert(item)

    def __len__(self):
        return self.len

    def __repr__(self):
        out = ""
        p = self.head
        while p != None:
            out += str(p) + ", "  # str(p) envokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def insert(self, val, first=False):
        node = Node(val)
        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node
        elif first == True:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

    def reverse(self):
        current = self.head
        previous = None

        if current == None:
            return

        while current.next != None:
            current.prev = current.next
            current.next = previous
            previous = current
            current = current.prev
        current.next = previous
        current.prev = None
        original_head = self.head
        self.head = self.tail
        self.tail = original_head

    def rotate(self, k):
        if k < self.len - k:
            for i in range(k):
                new_head = self.tail
                new_tail = self.tail.prev
                self.head.prev = self.tail
                new_head.next = self.head

                self.head = new_head
                self.tail = new_tail
                self.tail.next = None
                self.head.prev = None

        else:
            for i in range(len(self) - k):
                new_head = self.head.next
                new_tail = self.head
                new_tail.prev = self.tail

                self.head = new_head
                self.tail.next = new_tail
                self.tail = new_tail
                self.tail.next = None
                self.head.prev = None


    def delete_node(self, node):
        self.len -= 1
        if self.len == 0:
            self.head = None
            self.prev = None

        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        previous = node.prev
        next = node.next
        previous.next = next
        next.prev = previous


############
# QUESTION 6
############
# a
def prefix_suffix_overlap(lst, k):
    result = []
    n = len(lst)

    for i in range(n):
        beginning_list = lst[i]

        for j in range(n):
            if j != i:
                ending_list = lst[j]
                index_beginning = 0
                index_ending = len(ending_list) - k

                are_same = True

                for t in range(k):
                    if beginning_list[index_beginning] != ending_list[index_ending]:
                        are_same = False
                        break

                    index_beginning += 1
                    index_ending += 1
                if are_same == True:
                    result.append((i, j))
    return result





# c
#########################################
### Dict class ###
#########################################

class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        index = self.hash_mod(key)
        result = []
        for item in self.table[index]:
            if item[0] == key:
                result.append(item[1])
        return result


#########################################
### End Dict class ###
#########################################

# d
def prefix_suffix_overlap_hash1(lst, k):
    result = []
    d = Dict(len(lst))

    for i in range(len(lst)):
        key = lst[i][:k]
        d.insert(key, i)

    for i in range(len(lst)):
        suffix = lst[i][-k:]

        overlap = d.find(suffix)

        for j in overlap:
            if j != i:
                result.append((j, i))
    return result

# f
def prefix_suffix_overlap_hash2(lst, k):
    result = []
    d = {}

    for i in range(len(lst)):
        key = lst[i][:k]

        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]

    for i in range(len(lst)):
        suffix = lst[i][-k:]

        if suffix in d:
            for j in range(len(d[suffix])):
                if d[suffix][j] != i:
                    result.append((d[suffix][j], i))
    return result



########
# Tester
########

def test():
    # Testing Q1
    # Question 1
    p = Permutation([2, 3, 1, 0])
    if p.perm != [2, 3, 1, 0]:
        print("error in Permutation.__init__")
    q = Permutation([1, 0, 2, 4])
    if q.perm != None:
        print("error in Permutation.__init__")
    if p[0] != 2 or p[3] != 0:
        print("error in Permutation.__getitem__")

    p = Permutation([1, 0, 2])
    q = Permutation([0, 2, 1])
    r = p.compose(q)
    if r.perm != [1, 2, 0]:
        print("error in Permutation.compose")

    p = Permutation([1, 2, 0])
    invp = p.inv()
    if invp.perm != [2, 0, 1]:
        print("error in Permutation.inv")

    p1 = Permutation([1, 0, 2, 3])
    p2 = Permutation([2, 3, 1, 0])
    p3 = Permutation([3, 2, 1, 0])
    lst = [p1, p2, p3]
    q = compose_list(lst)
    if q.perm != [1, 0, 3, 2]:
        print("error in compose_list")

    identity = Permutation([0, 1, 2, 3])
    if identity.order() != 1:
        print("error in Permutation.order")
    p = Permutation([0, 2, 1])
    if p.order() != 2:
        print("error in Permutation.order")

    # Testing Q2
    # Question 2
    t = Binary_search_tree()
    if t.max_sum() != 0:
        print("error in Binary_search_tree.max_sum")
    t.insert('e', 1)
    t.insert('b', 2)
    if t.max_sum() != 3:
        print("error in Binary_search_tree.max_sum")
    t.insert('a', 8)
    t.insert('d', 4)
    t.insert('c', 10)
    t.insert('i', 3)
    t.insert('g', 5)
    t.insert('f', 7)
    t.insert('h', 9)
    t.insert('j', 6)
    t.insert('k', 5)
    if (t.max_sum() != 18):
        print("error in Binary_search_tree.max_sum")

    t = Binary_search_tree()
    if t.is_balanced() != True:
        print("error in Binary_search_tree.is_balanced")
    t.insert("b", 10)
    t.insert("d", 10)
    t.insert("a", 10)
    t.insert("c", 10)
    if t.is_balanced() != True:
        print("error in Binary_search_tree.is_balanced")
    t.insert("e", 10)
    t.insert("f", 10)
    if t.is_balanced() != False:
        print("error in Binary_search_tree.is_balanced")

    t2 = Binary_search_tree()
    t2.insert('c', 10)
    t2.insert('a', 10)
    t2.insert('b', 10)
    t2.insert('g', 10)
    t2.insert('e', 10)
    t2.insert('d', 10)
    t2.insert('f', 10)
    t2.insert('h', 10)
    if t2.diam() != 6:
        print("error in Binary_search_tree.diam")

    t3 = Binary_search_tree()
    t3.insert('c', 1)
    t3.insert('g', 3)
    t3.insert('e', 5)
    t3.insert('d', 7)
    t3.insert('f', 8)
    t3.insert('h', 6)
    t3.insert('z', 6)
    if t3.diam() != 5:
        print("error in Binary_search_tree.diam")

    # Testing Q3
    lst = DLList("abc")
    a = lst.head
    if a == None or a.next == None or a.next.next == None:
        print("error in DLList.insert")
    else:
        b = lst.head.next
        c = lst.tail
        if lst.tail.prev != b or b.prev != a or a.prev != None:
            print("error in DLList.insert")

    lst.insert("d", True)
    if len(lst) != 4 or lst.head.value != "d":
        print("error in DLList.insert")

    prev_head_id = id(lst.head)
    lst.reverse()
    if id(lst.tail) != prev_head_id or lst.head.value != "c" or lst.head.next.value != "b" or lst.tail.value != "d":
        print("error in DLList.reverse")

    lst.rotate(1)
    if lst.head.value != "d" or lst.head.next.value != "c" or lst.tail.value != "a":
        print("error in DLList.rotate")
    lst.rotate(3)
    if lst.head.value != "c" or lst.head.next.value != "b" or lst.tail.prev.value != "a":
        print("error in DLList.rotate")

    lst.delete_node(lst.head.next)
    if lst.head.next != lst.tail.prev or len(lst) != 3:
        print("error in DLList.delete_node")
    lst.delete_node(lst.tail)
    if lst.head.next != lst.tail or len(lst) != 2:
        print("error in DLList.delete_node")

    # Question 5
    s0 = "a" * 100
    s1 = "b" * 40 + "a" * 60
    s2 = "c" * 50 + "b" * 40 + "a" * 10
    lst = [s0, s1, s2]
    k = 50
    if prefix_suffix_overlap(lst, k) != [(0, 1), (1, 2)] and \
            prefix_suffix_overlap(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap")
    if prefix_suffix_overlap_hash1(lst, k) != [(0, 1), (1, 2)] and \
            prefix_suffix_overlap_hash1(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash1")
    if prefix_suffix_overlap_hash2(lst, k) != [(0, 1), (1, 2)] and \
            prefix_suffix_overlap_hash2(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash2")

