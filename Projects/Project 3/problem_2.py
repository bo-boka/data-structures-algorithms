
def rotated_array_search(input_list, number):
    """
    Find the index of a target value by searching in a rotated sorted array that has no duplicates.
    If not found return -1. Complexity should be O(log n).

    *Example of rotated array: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

    Notes: use modified binary search. When you cut in half, at least one of the halves will be sorted, which can be
    determined by comparing the lower & mid values. Can then compare those values with the target value to determine if
    the target is present in that half. Discarding half of the array with each recursion makes this O(log n).

    Args:
       input_list(array): Input array to search
       number(int): the target
    Returns:
       int: Index or -1
    """

    if len(input_list) == 0:
        return -1

    def rotated_binary(low, high):

        if low > high:
            return -1

        mid = (low + high)//2
        if input_list[mid] == number:
            return mid

        # left side is sorted
        if input_list[low] <= input_list[mid]:

            if input_list[low] <= number <= input_list[mid]:
                return rotated_binary(low, mid-1)
            else:
                return rotated_binary(mid+1, high)

        # right half is sorted
        else:

            if input_list[mid] <= number <= input_list[high]:
                return rotated_binary(mid+1, high)
            else:
                return rotated_binary(low, mid-1)

    return rotated_binary(0, len(input_list)-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# expected result Pass

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# expected result Pass

test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# expected result Pass

test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# expected result Pass

test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# expected result Pass

test_function([[], 10])
# expected result Pass

try:
    test_function([[6, 7, 8, 1, 2, 3, 4], 'prlenmd'])
except TypeError as e:
    print(f'''{type(e).__name__}: {e}''')
# expected result TypeError

try:
    test_function([False, 1])
except TypeError as e:
    print(f'''{type(e).__name__}: {e}''')
# expected result TypeError
