
import copy

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
    # Termination / Base conditionl
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


the_answer = deep_reverse([2,5,[6,3],7])
print('the answer: {}'.format(the_answer))
