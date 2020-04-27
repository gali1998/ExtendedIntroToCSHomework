from  skeleton import *

def get_random_string(k):
    rand_string = ""
    letters = ["a", "b", "c", "d"]

    return rand_string.join(random.choice(letters) for i in range(k))
