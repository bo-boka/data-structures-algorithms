
# =============== Bubble Sort =====================

def bubble_sort_1(array):

    length = len(array)
    sort = True
    while sort:
        count = 0
        for i in range(1, length):
            this = array[i]
            prev = array[i - 1]
            if this >= prev:
                continue

            array[i] = prev
            array[i - 1] = this

            count += 1
        if not count:
            sort = False

# wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
# bubble_sort_1(wakeup_times)
# print ("Pass" if (wakeup_times[0] == 3) else "Fail")


def bubble_sort_2(array):

    length = len(array)
    sort = True
    while sort:
        count = 0
        for i in range(1, length):
            this_hour, this_min = array[i]
            prev_hour, prev_min = array[i - 1]
            if this_hour < prev_hour or (this_hour == prev_hour and this_min < prev_min):
                continue

            array[i] = prev_hour, prev_min
            array[i - 1] = this_hour, this_min

            count += 1
        if not count:
            sort = False

# Entries are (h, m) where h is the hour and m is the minute
# sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]
# bubble_sort_2(sleep_times)
# print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")


# =============== Merge Sort =====================

def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list
    return merged


#test_list_1 = [8, 3, 1, 7, 0, 10, 2]
#test_list_2 = [1, 0]
#test_list_3 = [97, 98, 99]
#print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
#print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
#print('{} to {}'.format(test_list_3, mergesort(test_list_3)))


# =============== Count Inversions =====================

def count_inversions(arr):
    """
    Number of inversions in a disordered list is the # of pairs of elements that are inverted (out of order) in the list

    Here are some examples:
        [0,1] has 0 inversions
        [2,1] has 1 inversion (2,1)
        [3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
        [7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
    :param arr:
    :return:
    """
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start_index, mid_index)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)

    output = left_answer + right_answer

    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            count = count + (end_one - left_index + 1)  # left > right hence it's an inversion
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


# =============== Sort Case Sensitive String =====================

def case_sort(string):
    """
    Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort, that sorts
    uppercase and lowercase letters separately, such that if the  𝑖 th place in the original string had an uppercase char
    then it should not have a lowercase character after being sorted and vice versa.

    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """

    upper_ch_index = 0
    lower_ch_index = 0

    sorted_string = sorted(string)
    for index, character in enumerate(sorted_string):
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:  # ASCII value of a = 97 & ASCII value of z = 122, can also use isupper()
            lower_ch_index = index
            break

    output = list()
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)


# =============== Quick Sort =====================

def sort_a_little_bit(items, begin_index, end_index):
    """
    Compares pivot element (last element) with first element. If first is bigger,
    move first to last, move pivot to second to last, move second to last to first.
    :param items:
    :param begin_index:
    :param end_index:
    :return:
    """
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while pivot_index != left_index:

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index


def sort_all(items, begin_index, end_index):
    """
    Call the sorting mechanism on each side of the list where the pivot lands
    Note: Since quicksort is O(n^2) in the worst case (if you the array is already mostly sorted), you can randomize
    your pivot by choosing one in the middle and swapping it with the last index.
    :param items:
    :param begin_index:
    :param end_index:
    :return:
    """
    if end_index <= begin_index:
        return

    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quicksort(items):
    sort_all(items, 0, len(items) - 1)

# items = [8, 3, 1, 7, 0, 10, 2]
# quicksort(items)
# print(items)


# =============== Heap Sort =====================

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
    largest_index = i
    left_node = 2 * i + 1  # formula for left child node
    right_node = 2 * i + 2  # formula for right child node

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)


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


# array = [6,5,3,1,8,7,2,4]
# heapsort(array)
# print(array)


# =============== Sort 0,1,2's =====================

def sort_012(input_list):
    """
    Input list consisting of only 0s, 1s, and 2s, - sort it in a single traversal.
        Note that if you can get the function to put the 0s and 2s in the correct positions, this will automatically
        cause the 1s to be in the correct positions as well.
    :param input_list:
    :return:
    """
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1


# =============== Quick Select: Divide And Conquer rather than sort =====================

def quick_select(arr, k):
    """
    Find the k-th element of an unsorted array without sorting first, which would bring the average efficiency
    from O(n log(n)), using a sorting algo, to O(n) without sorting. Similar to QuickSort, worst case is O(n^2) and will
    be doing same functionality except only recurs the side that contains the k-th element. K represents the index+1
    (plus 1 since index starts at 0) you would want if the array was already sorted.
    We're using "Divide and Conquer" but only on part of the array instead of sorting the entire thing.

    Implement the algorithm explained above to find the k^th largest element in the given array

    :param arr:
    :param k:
    :return:
    """
    n = len(arr)  # length of the original array

    if 0 < k <= n:  # k should be a valid index
        # Helper variables
        set_of_medians = []
        arr_less_p = []
        arr_equal_p = []
        arr_more_p = []
        i = 0

        # Step 1 - Break arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to set_of_medians
        while i < n // 5:  # n//5 gives the integer quotient of the division
            median = find_median(arr, 5 * i, 5)  # find median of each group of size 5
            set_of_medians.append(median)
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if 5 * i < n:
            median = find_median(arr, 5 * i, n % 5)
            set_of_medians.append(median)

        # Step 3 - Find the median of set_of_medians
        if len(set_of_medians) == 1:  # Base case for this task
            pivot = set_of_medians[0]
        elif len(set_of_medians) > 1:
            pivot = quick_select(set_of_medians, (len(set_of_medians) // 2))

        # Step 4 - Partition the original arr into three sub-arrays
        for element in arr:
            if element < pivot:
                arr_less_p.append(element)
            elif element > pivot:
                arr_more_p.append(element)
            else:
                arr_equal_p.append(element)

        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if k <= len(arr_less_p):
            return quick_select(arr_less_p, k)

        elif k > (len(arr_less_p) + len(arr_equal_p)):
            return quick_select(arr_more_p, (k - len(arr_less_p) - len(arr_equal_p)))

        else:
            return pivot


# Helper function
def find_median(arr, start, size):
    my_list = []
    for i in range(start, start + size):
        my_list.append(arr[i])

        # Sort the array
    my_list.sort()

    # Return the middle element
    return my_list[size // 2]


# array = [33,3,2,8,5,1,22,7,75,24,50,58,40,45,27,2,9]
# print(quick_select(array, len(array)//2))
# Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
# k = 5
# print(quick_select(Arr, k))        # Outputs 12
