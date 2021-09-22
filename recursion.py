
import copy
import test


def sum_integers(n):
    """calculates sum of all integers from 1 to n
    """
    if n <= 0:
        return 0
    return sum_integers(n - 1) + n


def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n <= 1:
        return 1
    return n * factorial(n-1)


def reverse_string_rec(input):
    """
    Return reversed input string using recursion

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    if len(input) == 1:
        return input

    return reverse_string_rec(input[1:]) + input[0]

#recursion with true false
def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    # Termination / Base conditional
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        # if first and last char are identical and first/last chars were identical from the call before, return True
        # else return False
        return (first_char == last_char) and is_palindrome(sub_input)

def add_one(arr):
    """
    desc: adds one to a number that's represented in array form using recursion
    param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """

    #Base Case: recursion down to 1st array position
    if arr == [9]:
        return [1, 0]

    #Adds 1 & does not recur further
    if arr[-1] < 9:
        arr[-1] += 1
    #Every time it recurs further, 0 added spliced result
    else:
        arr = add_one(arr[:-1]) + [0]

    print(arr)
    return arr

#import copy @ top
def permute_list(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """

    outer_list = []
    if len(inputList) == 0:
        outer_list.append([])
        return outer_list

    first_val = inputList[0]
    rest_list = inputList[1:]
    temp_list = permute_list(rest_list)

    for a_list in temp_list:
        for j in range(0, len(a_list)+1):
            b_list = copy.deepcopy(a_list)
            b_list.insert(j, first_val)
            outer_list.append(b_list)
    return outer_list

def permute_string(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    """

    main_list = []
    if len(string) == 0:
        main_list.append(string)
        return main_list

    first_l = string[0]
    rest = string[1:]
    print(rest)
    temp_list = permute_string(rest)

    for a_str in temp_list:
        for x in range(0, len(a_str)+1):
            b_str = a_str[:x] + first_l + a_str[x:]
            print(b_str)
            main_list.append(b_str)
    return main_list

#string permutations from telephone pad combinations (2 following functions)
def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    """
    gets all string permutations from keypad number combinations. keypad order matters
    *Note that number 1 has no letters
    :param num: numbers selected on keypad
    :return: list of string permutations
    """
    output = list()
    if num <= 1:
        return ['']
    if 1 < num <= 9:
        return list(get_characters(num))
    last_val = num % 10
    temp = keypad(num//10)
    chars = get_characters(last_val)

    for c in chars:
        for t in temp:
            item = t + c
            output.append(item)
    return output

def deep_reverse_my_solution(arr):
    """
    reverse all the elements in a list & reverse element if it's a list
        -Begin with a blank final list to be returned.
        -Traverse the given list in the reverse order.
        -If an item in the list is a list itself, call the same function.
        -Otheriwse, append the item to the final list.
    :param arr: possible compound list
    :return: reversed list
    """

    if len(arr) == 0:
        return arr

    last_val = arr.pop()
    rest_vals = arr

    temp_arr = deep_reverse(rest_vals)

    if isinstance(last_val, list):
       deep_reverse(last_val)

    temp_arr.insert(0, last_val)
    return temp_arr

def deep_reverse_class_solution(arr):

    # Terminaiton / Base condition
    if len(arr) < 1:
        return arr

    reversed_items = []  # final list to be returned

    '''Traverse the given list (array) in the reverse direction using extended slice.'''
    for item in arr[::-1]:

        # If this item is a list itself, invoke deep_reverse to reverse the items recursively.
        if type(item) is list:
            item = deep_reverse(item)

        # append the item to the final list
        reversed_items.append(item)

    return reversed_items


def print_integers(n):
    if n == 0:
        return
    print(n)
    print_integers(n-1)

def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    """
    print steps to achieve tower of hanoi math problem.
        note that we're not using actual data structures because
        python with create those automatically in the call stack
    :param: num_disks - number of disks
    :param: source - beginning rod with disks
    :param: auxiliary - helper rod
    :param: destination - ending rod that should have disks
    """
    if num_disks == 0:
        return

    if num_disks == 1:
        print("{} {}".format(source, destination))
        return

    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)

def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')


def all_codes_get_alphabet(number):
    """
    Helper function to figure out alphabet equivalient of a number where a=1, b=2, etc.
        ASCII for lower case 'a' = 97 & chr(num) returns ASCII character a num
        So add 96 to the result of that function
    :param number: int 1-26 representing lower case alphabet
    :return: char equivalent of number
    """
    return chr(number + 96)

def all_codes(number):
    """
    find all sequential possibilities of ASCII lower case letters given
        a specific number where 1-26 represents the alphabet using recursion
    Notes: if a portion of the number is > 26, all other numbers are disregarded,
        will never need to include 3 digit sequences since only goes up to 26
    :param: number - input integer
    Return - list() of all codes possible for this number
    """

    if number == 0:
        return [""]

    # calculation for two right-most digits
    remainder = number % 100
    output_100 = list()
    if remainder <= 26 and number > 9:
        output_100 = all_codes(number//100)
        alpha_char = all_codes_get_alphabet(remainder)

        for index, element in enumerate(output_100):
            output_100[index] = element + alpha_char

    # calculation for right most digit
    remainder = number % 10

    output_10 = all_codes(number//10)
    alpha_char = all_codes_get_alphabet(remainder)

    for index, element in enumerate(output_10):
        output_10[index] = element + alpha_char

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output


def all_codes_test_function(attempt, expected_result):
    print('Actual Result from attempt: {}'.format(all_codes(attempt)))
    assert all_codes(attempt) == expected_result, str(attempt) + " should be [" + ', '.join(expected_result) + "]"


# all_codes_test_function(123, ["aw", "lc", "abc"])
# all_codes_test_function(145, ["ne", "ade"])
# all_codes_test_function(1457, ["neg", "adeg"])
# all_codes_test_function(1421, ["nu", "adu", "nba", "adba"])


def subsets(arr):
    """
    find all subsets of values in an array using recursion. Order of subsets in the output array is not
        important but the order of elements within a subset should remain the same as
        the input array.
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    """
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    """
    Called in above subsets() function
    """
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)
    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)
    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output

# test_function([9, 9], [[], [9], [9], [9, 9]], subsets)
# test_function([9, 12, 15], [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]], subsets)


def staircase(n):
    """
    Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many
    possible ways can you climb the staircase if the staircase has n steps?
        Examples:
            n == 3 then answer = 4 The output is 4 because there are four ways we can climb the stair-case:
                1 step + 1 step + 1 step
                1 step + 2 steps
                2 steps + 1 step
                3 steps
            n == 5 then answer = 13

    Note that a faster solution includes memoization

    param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    """
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Re
    # Recursive Step - Split the solution into base case if n > 3.

    if n <= 0:
        return 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

# test_function(3, 4, staircase)
test.test_function(5, 13, staircase)


def last_index(arr, target):
    """
    Given an array arr and a target element target , find the last index of occurrence of target in arr
    using recursion. If target is not present in arr , return -1 .
        For example:
            1. For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5 , output = 6
            2. For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7 , output = -1
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
        TODO: complete this method to find the last index of target in arr
    """
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    """
    Called from the above last_index() function
    """
    if index < 0:
        return -1
    # check if target is found
    if arr[index] == target:
        return index
    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)


