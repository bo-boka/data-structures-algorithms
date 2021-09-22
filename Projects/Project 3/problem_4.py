
def sort_012(input_list):
    """
    AKA Dutch National Flag Problem
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
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# expected result Pass

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# expected result Pass

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# expected result Pass

test_function([])
# expected result Pass

test_function([1, 1, 1, 1, 1])
# expected result Pass

test_function([0, 0, 0, 0, 0, 0])
# expected result Pass

test_function([2, 2, 2, 2, 2, 2])
# expected result Pass

try:
    test_function([1,3,4,3,7,3,8])
except ValueError as e:
    print(e)
# expected result ValueError

try:
    test_function([1, 0, 0, 2, 0, 1, False, 0, 2])
except Exception as e:
    print(e)
# expected result TypeError
