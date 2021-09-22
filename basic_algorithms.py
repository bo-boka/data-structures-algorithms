

# ===================== Binary Searches ========================

def binary_search_find_idx_w_loops(input_list, target):
    """
    Find the index of the target value in the array using loops.
    If the target value is not present in the array, return -1.
    :param input_list: sorted array of integers
    :param target: integer to search for
    :return: index of target value. -1 for not found
    """

    lower = 0
    upper = len(input_list) - 1
    while upper >= lower:
        center = (lower + upper) // 2
        center_val = input_list[center]
        if center_val == target:
            return center
        if target > center_val:
            lower = center+1
        else:
            upper = center-1
    return -1


def binary_search_find_idx_recursive_1(input_list, target):
    """
    Find the index of the target value in the array using recursion.
    If the target value is not present in the array, return -1.
    :param input_list: sorted array of integers
    :param target: integer to search for
    :return: index of target value. -1 for not found
    """

    low = 0
    up = len(input_list) - 1

    def b_s_r(lower, upper):

        center = (lower + upper)//2
        center_val = input_list[center]

        if lower > upper:
            return -1
        elif target > center_val:
            return b_s_r(center+1, upper)
        elif target < center_val:
            return b_s_r(lower, center-1)
        else:
            return center

    return b_s_r(low, up)


def binary_search_find_idx_recursive_2(target, source, left=0):
    """
    Find the index using recursion, alternative & recommended.
    :param target:
    :param source:
    :param left:
    :return: index of target value. -1 for not found.
    """
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return binary_search_find_idx_recursive_2(target, source[center+1:], left+center+1)
    else:
        return binary_search_find_idx_recursive_2(target, source[:center], left)


def binary_search_contains(target, source):
    """
    Determines if target exists in list
    :param target: value to search
    :param source: sorted array of integers
    :return: Bool depending on if value exists
    """
    if len(source) == 0:
        return False
    center = (len(source)-1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return binary_search_contains(target, source[center+1:])
    else:
        return binary_search_contains(target, source[:center])


def binary_search_first_repeated_value_recursive(binary_search, input_list, target):
    """
    Find first occurrence of a value that occurs more than once in a sorted array using binary search
    :param binary_search: function that finds target using binary search
    :param input_list: sorted list of values
    :param target: integer to find first occurrence of
    :return: index of first occurrence of target value
    """
    # make original binary search the upper bound
    # cut at center
    # if center == target
        # set it as new upper bound
    # else
        # set as lower bound
    # keep doing this until upper & lower cross, left over index is the target

    low = 0
    up = binary_search(input_list, target)  # want lowest instance of the target, so remove rest of list
    if up == -1:
        return -1

    def find_first(lower, upper):

        if upper == lower:
            return upper
        center = (lower + upper)//2
        cntr_val = input_list[center]
        if cntr_val == target:
            return find_first(lower, center)
        else:
            return find_first(center+1, upper)

    return find_first(low, up)


def first_and_last_index_1(input_list, target):
    """
    Find indices of first & last occurrence of a value that occurs more than once in a sorted array using binary search
    :param input_list: sorted list of values that may contain duplicates
    :param target: integer to find first and last occurrence of
    :return: array of first and last indices
    """

    def find_first_last(lower, upper, first_trigger):

        # after finishing search, last idx to check will either be lowest target or return -1 if doesn't exist in list
        if upper == lower:
            if input_list[upper] == target:
                return upper
            else:
                return -1

        center = (lower + upper)//2 if first_trigger else (lower + upper)//2 + 1
        if center > len(input_list)-1:
            return -1
        cntr_val = input_list[center]

        # if we find the target, check trigger to see if we're looking for first or last & set bounds accordingly
        if cntr_val == target:
            if first_trigger:
                return find_first_last(lower, center, first_trigger)
            else:
                return find_first_last(center, upper, first_trigger)
        # else resume standard binary search
        elif target > cntr_val:
            return find_first_last(center+1, upper, first_trigger)
        else:
            return find_first_last(lower, center-1, first_trigger)

    first = find_first_last(0, len(input_list)-1, True)
    last = find_first_last(0, len(input_list)-1, False)

    return [first, last]

# def binary_search_first_and_last_repeated_values(input_list, target):
# print(first_and_last_index_1([1,2,2,2,2,2,2,3,3,3,3,3,4,4, 5,5,5,5,8,9,10], 12))


def first_and_last_index_2(arr, number):

    def find_start_index(arr, number, start_index, end_index):
        # binary search solution to search for the first index of the array
        if start_index > end_index:
            return -1

        mid_index = start_index + (end_index - start_index) // 2

        if arr[mid_index] == number:
            current_start_pos = find_start_index(arr, number, start_index, mid_index - 1)
            if current_start_pos != -1:
                start_pos = current_start_pos
            else:
                start_pos = mid_index
            return start_pos

        elif arr[mid_index] < number:
            return find_start_index(arr, number, mid_index + 1, end_index)
        else:
            return find_start_index(arr, number, start_index, mid_index - 1)

    def find_end_index(arr, number, start_index, end_index):
        # binary search solution to search for the last index of the array
        if start_index > end_index:
            return -1

        mid_index = start_index + (end_index - start_index) // 2

        if arr[mid_index] == number:
            current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
            if current_end_pos != -1:
                end_pos = current_end_pos
            else:
                end_pos = mid_index
            return end_pos
        elif arr[mid_index] < number:
            return find_end_index(arr, number, mid_index + 1, end_index)
        else:
            return find_end_index(arr, number, start_index, mid_index - 1)

    # search first occurrence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)

    # search last occurrence
    last_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def pair_sum(arr, target):
    """
    Find two numbers such that their sum is equal to the target w/o using extra space (data structures)
    Return the two numbers in the form of a sorted list
    :param: arr - input array
    :param: target - target value
    :return: list of two numbers
    """
    # sort the list
    arr.sort()

    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(arr) - 1

    # shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:  # sum < target ==> shift front pointer forward
            front_index += 1
        else:
            back_index -= 1  # sum > target ==> shift back pointer backward

    return [None, None]

# input_list = [2, 7, 11, 15, 4, 1]
# [1,2,4,7,11,15]
# [1,2,3,4,5,6]
# print(pair_sum(input_list, 12))


# ========================= Maximum Sub-Array ================================

# Helper Function - Find the max crossing sum w.r.t. middle index
def max_crossing_sum(arr, start, mid, stop):
    # LEFT PHASE - Traverse the Left part starting from mid element
    left_sum = arr[mid]  # Denotes the sum of left part from mid element to the current element
    left_max_sum = arr[mid]  # Keep track of maximum sum

    # Traverse in reverse direction from (mid-1) to start
    for i in range(mid - 1, start - 1, -1):  # The 2nd argument of range is not inclusive. 3rd argument is the step size
        left_sum = left_sum + arr[i]
        if left_sum > left_max_sum:  # Update leftMaxSum
            left_max_sum = left_sum

    # RIGHT PHASE - Traverse the Right part, starting from (mid+1)
    right_sum = arr[mid + 1]  # Denotes the sum of right part from (mid+1) element to the current element
    right_max_sum = arr[mid + 1]  # Keep track of maximum sum

    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid + 2, stop + 1):  # The second argument of range is not inclusive
        right_sum = right_sum + arr[j]
        if right_sum > right_max_sum:  # Update rightMaxSum
            right_max_sum = right_sum

    # Both left_max_sum and lefttMaxSum each would contain value of atleast one element from the arr
    return right_max_sum + left_max_sum


# Recursive function
def max_subarray_recursive(arr, start, stop):  # start and stop are the indices
    # Base case
    if start == stop:
        return arr[start]

    if start < stop:
        mid = (start + stop) // 2  # Get the middle index
        L = max_subarray_recursive(arr, start, mid)  # Recurse on the Left part
        R = max_subarray_recursive(arr, mid + 1, stop)  # Recurse on the Right part
        C = max_crossing_sum(arr, start, mid, stop)  # Find the max crossing sum w.r.t. middle index
        return max(C, max(L, R))  # Return the maximum of (L,R,C)

    else:  # If ever start > stop. Not feasible.
        return nums[start]


def max_subarray(arr):
    """
    Finds the maximum sum of contiguous subarray among all the possible subarrays.
    O(nlogn) time, using Divide and Conquer approach
    :param arr: array
    :return: integer sum
    """
    start = 0  # staring index of original array
    stop = len(arr) - 1  # ending index of original array
    return max_subarray_recursive(arr, start, stop)


# arr = [-2, 7, -6, 3, 1, -4, 5, 7]
# print("Maximum Sum = ", max_subarray(arr))  # Outputs 13


# ========================= Find Square Root (Floored) ================================

def sqrt(number):
    """
    Calculate the floored square root of a number with the expected time complexity of O(log(n))

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    def sqrt_recursive(low, high, num):

        if type(number) != int:
            raise TypeError("The value entered is not a number.")
        if number == 0:
            return 0
        if number == 1:
            return 1

        mid = (low + high) // 2

        if num // mid == mid:
            return mid
        elif num // mid > mid:
            return sqrt_recursive(mid+1, high, num)
        else:
            return sqrt_recursive(low, mid-1, num)

    return sqrt_recursive(0, number, number)


#print ("Pass" if  (3 == sqrt(9)) else "Fail")
#print ("Pass" if  (0 == sqrt(0)) else "Fail")
#print ("Pass" if  (4 == sqrt(16)) else "Fail")
#print ("Pass" if  (1 == sqrt(1)) else "Fail")
#print ("Pass" if  (5 == sqrt(27)) else "Fail")
#print ("Pass" if  (5 == sqrt(25)) else "Fail")


# ========================= Find Number in Rotated Array ================================

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

'''
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
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
'''


# ========================= Rearrange Array for Maximum Sum ================================

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two-number array such that their sum is maximum. Assume that all elements
    are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. Use O(n log n)
    complexity without using any sorting function that Python provides.
    E.g.: For [1, 2, 3, 4, 5], the expected answer would be [531, 42]. Another expected answer can be [542, 31].
    In scenarios such as these when there are more than one possible answers, return any one.

    Steps:
        -sort input list from max to min with an O(n log n) algorithm
            -mergesort would work, but heapsort would save space if there are no duplicates
            -if there are duplicates, heapsort is less stable because it may switch elements having same value
        -iterate sorted list using modulus to deal elements into two strings
        -convert strings to integers and put inside list

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # input validation before function definitions to save space
    if len(input_list) < 2:
        raise ValueError("input_list has less than 2 elements.")

    for j in range(len(input_list)-1):
        if type(input_list[j]) is not int:
            raise ValueError("List contains non-integer at index: {}.".format(j))

    if len(input_list) == 2:
        return input_list

    def heapify(arr, n, i):
        """
        :param: arr - array to heapify
        n -- number of elements in the array
        i -- index of the current node
        TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
        """

        # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
        # and find the largest value.   If one of the children is larger swap the values and recurse into that subtree

        # consider current index as largest
        smallest_index = i
        left_node = 2 * i + 1  # formula for left child node
        right_node = 2 * i + 2  # formula for right child node

        # compare with left child
        if left_node < n and arr[i] > arr[left_node]:
            smallest_index = left_node

        # compare with right child
        if right_node < n and arr[smallest_index] > arr[right_node]:
            smallest_index = right_node

        # if either of left / right child is the smallest node
        if smallest_index != i:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

            heapify(arr, n, smallest_index)

    def heapsort(arr):
        """
        Convert array to heap tree, which sorts as added. Then convert back to array.
        :param arr:
        :return:
        """
        # First convert the array into a maxheap by calling heapify on each node, starting from the end
        # now that you have a maxheap, you can swap the first element (largest) to the end (final position)
        # and make the array minus the last element into maxheap again.  Continue to do this until the whole
        # array is sorted
        n = len(arr)

        # Build a maxheap.
        for i in range(n, -1, -1):
            heapify(arr, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            heapify(arr, i, 0)

    heapsort(input_list)

    num_1 = num_2 = ''
    for j in range(len(input_list)):
        if j % 2 == 0:
            num_1 += str(input_list[j])
        else:
            num_2 += str(input_list[j])

    return [int(num_1), int(num_2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

'''
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6], [4, 6]])
try:
    test_function([[], []])
except ValueError as e:
    print(e)

try:
    test_function([[False, False, False], []])
except ValueError as e:
    print(e)
'''


# =============== Sort 0,1,2's =====================

def sort_012(input_list):
    """
    Aka Dutch National Flag Problem
    Input list consisting of only 0s, 1s, and 2s, - sort it in a single traversal.
        Note that if you can get the function to put the 0s and 2s in the correct positions, this will automatically
        cause the 1s to be in the correct positions as well.
    :param input_list:
    :return:
    """

    if len(input_list) == 0:
        return input_list

    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1
    front_index = 0

    while front_index <= next_pos_2:
        if type(input_list[front_index]) is not int:
            raise TypeError("Input list contains non-integer value(s).")
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        elif input_list[front_index] == 1:
            front_index += 1
        else:
            raise ValueError("Input list contains values greater than 2 or less than 0.")

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

'''
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
'''


# =============== Min & Max Linearly =====================

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

    print(val)
    return min_int, max_int


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
