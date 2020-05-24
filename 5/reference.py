# Skeleton file for HW5 - Spring 2019 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to your ID number (extension .py).


############
# QUESTION 1
############

class Permutation:
    def __init__(self, perm):
        def check_viability(lst):
            res = ["a" for i in range(0, len(lst))]
            for i in range(0, len(lst)):
                ind = lst[i]
                if ind >= len(lst):
                    return None

                if res[ind] == "a":
                    res[ind] = 1
                elif res[ind] == 1:
                    return None

            if "a" in res:
                return None
            else:
                return lst

        self.perm = check_viability(perm)

    def __getitem__(self, i):
        return self.perm[i]

    def compose(self, other):
        res = []
        for i in range(0, len(self.perm)):
            res += [self[other[i]]]
        return Permutation(res)

    def inv(self):
        res = ["a" for i in range(0, len(self.perm))]
        for i in range(0, len(self.perm)):
            ind = self[i]
            res[ind] = i
        return Permutation(res)

    def __eq__(self, other):
        return self.perm == other.perm

    def __ne__(self, other):
        return self.perm != other.perm

    def order(self):
        example = Permutation([i for i in range(0, len(self.perm))])
        res = Permutation([self.perm[i] for i in range(0, len(self.perm))])
        cnt = 1
        while res != example:
            res = self.compose(res)
            cnt += 1
        if res == example:
            return cnt


# This function is not part of the class Permutation

def compose_list(lst):
    new_lst = []
    for i in range(0, len(lst)):
        new_lst.append(lst[i])
    return compose_list_rec(new_lst)


def compose_list_rec(lst):
    if len(lst) == 2:
        return lst[0].compose(lst[1])
    else:
        new_last = lst[len(lst) - 2].compose(lst[len(lst) - 1])
        lst.pop(len(lst) - 1)
        lst[len(lst) - 1] = new_last
        return compose_list_rec(lst)

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
        def max_sum_rec(node):
            res = 0
            if node.left == None and node.right == None:
                return node.val
            elif node.left == None and node.right != None:
                return node.val + max_sum_rec(node.right)
            elif node.left != None and node.right == None:
                return node.val + max_sum_rec(node.left)
            elif node.left != None and node.right != None:
                right_sum = max_sum_rec(node.right)
                left_sum = max_sum_rec(node.left)
                if right_sum <= left_sum:
                    return node.val + left_sum
                elif right_sum > left_sum:
                    return node.val + right_sum

        if self.root == None:  # empty tree
            result = 0
        else:
            result = max_sum_rec(self.root)
        return result

    def is_sorted(self):
        def is_sorted_rec(node):
            if node.left == None and node.right == None:
                # Bottom of the Tree
                min_val = node.val
                max_val = node.val
                return [True, max_val, min_val]
                # In each node we'll store the minimum and maximum value of subtree
            elif node.left == None and node.right != None:
                # If there's only a right next node, compares her value with the
                # current one and checks if the tree hanging from it is sorted
                if node.val <= node.right.val and is_sorted_rec(node.right)[0]:
                    if node.val <= is_sorted_rec(node.right)[2]:
                        # Checking that there's no node in the rest of the subtree that has a larger value
                        # than the current one
                        return [True, is_sorted_rec(node.right)[1], node.val]
                    else:
                        return [False, is_sorted_rec(node.right)[1], node.val]
                else:
                    return [False, 0, 0]
            elif node.left != None and node.right == None:
                # If there's only a Left next node, compares her value with the
                # Current one and checks if the tree hanging from it is sorted

                if node.val >= node.left.val and is_sorted_rec(node.left)[0]:
                    if node.val >= is_sorted_rec(node.left)[1]:
                        return [True, node.val, is_sorted_rec(node.left)[2]]
                    else:
                        return [False, node.val, is_sorted_rec(node.left)[2]]
                else:
                    return [False, 0, 0]
            elif node.left != None and node.right != None:
                # If there's both a right and a left next node,
                # compares their values value with the current one and checks if the trees hanging
                # from them are sorted
                if node.val >= node.left.val and is_sorted_rec(node.left)[0] and node.val <= node.right.val and \
                        is_sorted_rec(node.right)[0]:
                    new_max_val = max(is_sorted_rec(node.right)[1], is_sorted_rec(node.left)[1])
                    new_min_val = min(is_sorted_rec(node.right)[2], is_sorted_rec(node.left)[2])
                    if node.val >= is_sorted_rec(node.left)[1] and node.val <= is_sorted_rec(node.right)[2]:
                        return [True, new_max_val, new_min_val]
                    else:
                        return [False, new_max_val, new_min_val]

                else:
                    return [False, 0, 0]

        if self.root == None:  # empty tree
            result = True
        else:
            result = is_sorted_rec(self.root)[0]

        return result

    def is_balanced(self):

        def is_balanced_rec(node):
            # We would like this function to check the depth of the tree AND if it's balanced at
            # the same time. The result of this function for each node will be the depth of the
            # longest tree hanging from it, and if the tree starting from the CURRENT node
            # is balanced.
            if node.left == None and node.right == None:
                # Reached a leaf, default value is True and the depth count is 0
                return [True, 0]
            elif node.left == None and node.right != None:
                # In each one of the option where ther'e s child to the current node,
                # the viability indicator chaeck if the tree hanging from this node is
                # balanced. If not, that's all that matters and the 0 index of the result list
                # will always be kept at False
                depth = is_balanced_rec(node.right)[1]
                viability = is_balanced_rec(node.right)[0]
                if viability == True:
                    # In case the tree hanging from the right node is balanced, the
                    # viability indicator stays True and the depth for this tree is increased
                    # by 1. Now the result represents the tree starting from this node.
                    if depth > 0:
                        return [False, depth + 1]
                    else:
                        return [True, depth + 1]
                else:
                    return [False, depth + 1]
            elif node.left != None and node.right == None:
                # Same as with the right-child-only node
                depth = is_balanced_rec(node.left)[1]
                viability = is_balanced_rec(node.left)[0]
                if viability == True:
                    if depth > 0:
                        return [False, depth + 1]
                    else:
                        return [True, depth + 1]
                else:
                    return [False, depth + 1]
            elif node.left != None and node.right != None:
                # In case there are two trees hanging from it, will check if BOTH
                # are viable. If so, will find the maximum depth between the two and update
                # the depth of the current tree starting from that node.
                depth_left = is_balanced_rec(node.left)[1]
                viability_left = is_balanced_rec(node.left)[0]
                depth_right = is_balanced_rec(node.right)[1]
                viability_right = is_balanced_rec(node.right)[0]
                maximum_depth = max(depth_left, depth_right)
                minimum_depth = min(depth_left, depth_right)
                if viability_right and viability_left:
                    if maximum_depth - minimum_depth <= 1:
                        return [True, maximum_depth + 1]
                    else:
                        return [False, maximum_depth + 1]
                else:
                    return [False, depth_left]

        # The importance of the envelope function is that the Method will return
        # only the balanced-indicator value and not the depth. Also, to check an empty tree.
        if self.root == None:  # empty tree
            result = True
        else:
            result = is_balanced_rec(self.root)[0]
        return result

    def diam(self):
        # Defining the inner depth function, that applies on nodes and not Trees.
        # This time starting from 0, because we count nodes and not steps
        def depth_rec_copy(node):
            if node == None:
                return 0
            else:
                return 1 + max(depth_rec_copy(node.left), depth_rec_copy(node.right))

        # Now for the recursive Diameter function itself
        def diam_rec(node):
            # Base case:
            if node == None:
                return 0

            # Finding height of left and right trees, for example for cases
            # when there's no split
            left_tree_height = depth_rec_copy(node.left)
            right_tree_height = depth_rec_copy(node.right)

            # Finding diameters of left and right trees
            left_tree_diam = diam_rec(node.left)
            right_tree_diam = diam_rec(node.right)

            # Calculating the path from two longest walks, one starting from
            # left and the other from right, including current node
            current_diam = left_tree_height + right_tree_height + 1

            # Longest between the diameters of two sub trees
            max_sub_tree_diam = max(right_tree_diam, left_tree_diam)

            # Finding the maximal between all
            return max(current_diam, max_sub_tree_diam)

        if self.root == None:  # empty tree
            result = 0
        else:
            result = diam_rec(self.root)
        return result


############
# QUESTION 3
############
# a
def prefix_suffix_overlap(lst, k):
    res = []
    for i in range(0, len(lst)):
        prefix = lst[i][0:k]
        for j in range(0, len(lst)):
            suffix = lst[j][-k:]
            if prefix == suffix and i != j:
                res.append((i, j))
    return res


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
        res = []
        i = self.hash_mod(key)
        for item in self.table[i]:
            if item[0] == key:  # Avoiding collisions
                res.append(item[1])
        return res


#########################################
### End Dict class ###
#########################################

# d
def prefix_suffix_overlap_hash1(lst, k):
    dictionary = Dict(len(lst))
    res = []
    for i in range(0, len(lst)):
        # Going through all the strings once to take prefixes
        prefix = lst[i][0:k]  # Determining the prefix of said string
        dictionary.insert(prefix, i)  # Adding the prefix to the dictionary in it's right places
    for j in range(0, len(lst)):
        # Going through all the strings to determine suffixes
        suffix = lst[j][-k:]
        # Searching the dictionary for a place with this suffix as a key
        prefix_locations = dictionary.find(suffix)
        for num in prefix_locations:
            # All the numbers in this place in the dictionary represent indexes where
            # this string appeared as a suffix, so now we'll add to the results all the
            # pairs of prefix index and suffix index
            if num != j:  # Same string
                res.append((num, j))
    return res


# f
def prefix_suffix_overlap_hash2(lst, k):
    dictionary = {}
    res = []
    for i in range(0, len(lst)):
        # Going through all the strings once to take prefixes
        prefix = lst[i][0:k]  # Determining the prefix of said string
        if prefix in dictionary:
            dictionary[prefix].append(i)
        else:
            dictionary[prefix] = [i]
    for j in range(0, len(lst)):
        # Going through all the strings to determine suffixes
        suffix = lst[j][-k:]
        # Going to that slot in the dictionary to get all indexes with stored prefix
        if suffix in dictionary:
            for ind in range(0, len(dictionary[suffix])):
                # Adding each and every one from the slot
                if dictionary[suffix][ind] != j:  # Same string
                    res.append((dictionary[suffix][ind], j))
    return res


###########
# QUESTION 4
############

def next_row(lst):
    res = [1]
    for i in range(0, len(lst) - 1):
        num = lst[i] + lst[i + 1]
        res.append(num)
    res.append(1)
    return res


# b
def generate_pascal():
    yield [1]
    lst = [1]
    while True:
        new_lst = next_row(lst)
        yield new_lst
        lst = new_lst


# c

def bernoulli_line(lst):
    # Recieves a list from Pascal triangle and calculates it's line on Bernoulli
    res = [1]
    num = 1
    for i in range(1, len(lst)):
        num += lst[i]
        res.append(num)
    return res


def generate_bernoulli():
    pascal_line = generate_pascal()
    while True:
        current_line = next(pascal_line)
        yield bernoulli_line(current_line)


########
# Tester
########

def test():
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

    t1 = Binary_search_tree()
    if t1.is_sorted() != True:
        print("error in Binary_search_tree.is_sorted")
    t1.insert('e', 5)
    t1.insert('b', 2)
    t1.insert('a', 1)
    t1.insert('d', 4)
    t1.insert('c', 4)
    if t1.is_sorted() != True:
        print("error in Binary_search_tree.is_sorted")
    t1.insert('c', 40)
    if t1.is_sorted() != False:
        print("error in Binary_search_tree.is_sorted")

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

    # Question 3
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

    # Question 4
    gp = generate_pascal()
    if gp == None:
        print("error in generate_pascal()")
    elif next(gp) != [1] or next(gp) != [1, 1] or next(gp) != [1, 2, 1]:
        print("error in generate_pascal()")
