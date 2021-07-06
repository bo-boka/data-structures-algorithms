

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
    Find the index using recursion, alternative.
    :param target:
    :param source:
    :param left:
    :return:
    """
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


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
print(first_and_last_index_1([1,2,2,2,2,2,2,3,3,3,3,3,4,4, 5,5,5,5,8,9,10], 12))


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


arr = [-2, 7, -6, 3, 1, -4, 5, 7]
print("Maximum Sum = ", max_subarray(arr))  # Outputs 13
