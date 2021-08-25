
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers in O(n) without using Python inbuilt functions.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        raise ValueError("Input list is empty.")

    min_int = ints[0]
    max_int = ints[0]

    for i in range(len(ints)):
        val = ints[i]
        if type(val) is not int:
            raise TypeError("Input list contains non-integer value(s).")
        if val < min_int:
            min_int = val
        if val > max_int:
            max_int = val

    return min_int, max_int


# ======== testing section =========

import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# expected result: Pass

print(get_min_max([1, 1, 1, 1, 1, 1, 1]))
# expected result: (1, 1)

print(get_min_max([1, 2, 3, 4, 5, 6, 7]))
# expected result: (1, 7)

print(get_min_max([7, 6, 5, 4, 3, 2, 1]))
# expected result: (1, 7)

try:
    print(get_min_max([]))
except ValueError as e:
    print(e)
# expected result: ValueError

try:
    print(get_min_max(['roller', 'fe', 'cat', 'andy', 'done', 'bird']))
except TypeError as e:
    print(e)
# expected result: TypeError

print(get_min_max([1, -1, 7, -7, 0, 1, 9999999999, 10, 2]))
# expected result: (-7, 9999999999)

