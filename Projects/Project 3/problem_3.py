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

    # input checks put before function definitions to save space
    if len(input_list) < 2:
        raise ValueError("input_list has less than 2 elements.")

    for j in range(len(input_list)-1):
        if type(input_list[j]) is not int:
            raise TypeError("List contains non-integer at index: {}.".format(j))

    if len(input_list) == 2:
        return input_list

    def heapify(arr, n, i):
        """
        :param: arr - array to heapify
        n -- number of elements in the array
        i -- index of the current node
        Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
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


test_function([[1, 2, 3, 4, 5], [542, 31]])
# expected result Pass

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# expected result Pass

test_function([[4, 6], [4, 6]])
# expected result Pass

try:
    test_function([[], []])
except ValueError as e:
    print(e)
# expected result ValueError

try:
    test_function([[False, False, False], []])
except TypeError as e:
    print(e)
# expected result TypeError
