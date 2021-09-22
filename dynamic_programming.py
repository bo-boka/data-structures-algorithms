import collections
import pprint


# ===================== Fibonacci - Bottom Up Approach =============================

def factorial_tabulation(number):
    """
    Factorial is the product of an integer and all the ints below it. Represented with an exclamation after number.
    Example: 4! = 24

    Bottom-Up Approach includes iteration and tabulation.

    :param number: integer to find factorial for
    :return: factorial of integer
    """

    # initialize data table. 0th must be 1, but others will be overwritten
    dt = [1 for _ in range(number+1)]

    # sequentially populate data table
    for i in range(1, number+1):
        dt[i] = dt[i-1] * i

    return dt[-1]


# print(factorial_tabulation(4))


# ===================== Staircase - Top Down Approach =============================


def staircase_memoization(number):
    """
    A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps at a time. Given that the staircase
    has a total n steps, write a function to count the number of possible ways in which child can run up the stairs.
    Example: if n = 5, answer is 13

    Top-Down Approach includes recursion and memoization.

    :param number: integer of steps in staircase
    :return: integer of number combinations
    """

    def sc_recur(n):
        if n == 1:
            output = 1
        elif n == 2:
            output = 2
        elif n == 3:
            output = 4
        else:
            if (n - 1) in num_dict:
                first_output = num_dict[n - 1]
            else:
                first_output = sc_recur(n - 1)

            if (n - 2) in num_dict:
                second_output = num_dict[n - 2]
            else:
                second_output = sc_recur(n - 2)

            if (n - 3) in num_dict:
                third_output = num_dict[n - 3]
            else:
                third_output = sc_recur(n - 3)

            output = first_output + second_output + third_output

        # cache calculation to avoid recomputation
        num_dict[n] = output
        return output

    num_dict = dict({})
    return sc_recur(number)


# print(staircase_memoization(5))


# ===================== Knapsack Problem (Multiple Solutions) =============================

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


def knapsack(weight_limit, items):
    """
    A problem in combinatorial optimization. Given a knapsack that can only carry a certain amount of weight and a list
    of items with an associated weight and value for each, find the max value of items that the knapsack can carry
    without exceeding the weight limit.

    This is a greedy algorithm that uses dynamic programming to achieve optimal time complexity. We're using recursion
    to break the problem into smaller sub-problems and then using memoization to store the max value in a dictionary for
    a certain remaining capacity called with a certain index.

    Because we're only calling the function once for each capacity-index combination, and the capacity is an integer
    rather than a list size, the time complexity is O(nW) where n is the number of items and W is the weight limit. The
    complexity is pseudo-polynomial for those reasons. The data structure reduces the complexity from exponential.

    :param weight_limit: max capacity
    :param items: list of named tuples with weight and value
    :return: max value
    """

    def ks_recur(capacity, idx):
        """
        Use recursion to find and store the max value for each combination of indices with remaining capacity.

        :param capacity: remaining capacity left
        :param idx: current index of items list
        :return: max value
        """

        # if combo already exists in cache, return that
        if (capacity, idx) in cache.keys():
            return cache[(capacity, idx)]

        # base case where capacity has been met or sequence has been traversed
        if capacity <= 0 or idx < 0:
            return 0

        # if current item weight will exceed capacity, do not add it
        if items[idx].weight > capacity:
            result = ks_recur(capacity, idx-1)
        # find max value for item added vs not added
        else:
            val_a = items[idx].value + ks_recur(capacity-items[idx].weight, idx-1)
            val_b = ks_recur(capacity, idx-1)
            result = max(val_a, val_b)

        # add combo to cache before returning max result
        cache[(capacity, idx)] = result
        return result

    cache = dict()
    last_idx = len(items)-1
    max_value = ks_recur(weight_limit, last_idx)
    return max_value

'''
items_2 = [Item(10, 7), Item(9, 8), Item(5, 6)]
print(knapsack(15, items_2))

items = [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]
print(knapsack(25, items))
'''


# ===================== Levenshtien Distance - BUA =============================

def l_d(str_a, str_b):
    """
    Aka Edit Distance problem. Calculate the edit distance between 2 strings, i.e. minimum number of operations it'll
    take to transform one string into the other.
    Three possible operations:
        1. Replace char
        2. Delete char
        3. Insert char
    :param str_a:
    :param str_b:
    :return:
    """
    pass


# ===================== Longest Common Subsequence - BUA =============================

def lcs_tabulation(string_a, string_b):
    """
    Use the Bottom Up Approach to determine longest sequence of letters that are present in both the given two strings
    in the same relative order but needn't be a contiguous substring.

    A subsequence is a set of characters that need not be a contiguous substring.
    E.g. 'ABC' is a subsequence of 'AXBYC' but not a substring.

    O(nm) or O(n^2) time complexity.

    Note: the Bottom Up Approach is not intuitive at all, which means the logic isn't easy to decipher.

    :param string_a: 1st string
    :param string_b: 2nd string
    :return: length of longest common subsequence
    """

    # initialize the matrix
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]

    # enumerate(str) returns a tuple containing the index and character in each iteration
    for i_a_row, char_a in enumerate(string_a):

        for i_b_col, char_b in enumerate(string_b):

            # If there is a match,
            # fill that grid cell with the value to the diagonal/top-left of that cell plus one
            if char_a == char_b:
                lookup_table[i_a_row + 1][i_b_col + 1] = lookup_table[i_a_row][i_b_col] + 1

            # If there is not a match,
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[i_a_row + 1][i_b_col + 1] = max(
                    # top cell
                    lookup_table[i_a_row][i_b_col + 1],
                    # left cell
                    lookup_table[i_a_row + 1][i_b_col])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]

'''
# Tests
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs_tabulation(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs_tabulation(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
'''


# ===================== Longest Common Subsequence - TDA =============================

def lcs_memoization(string_a, string_b):
    """
    Use the Top Down Approach to determine longest sequence of letters that are present in both the given two strings
    in the same relative order but needn't be a contiguous substring.

    A subsequence is a set of characters that need not be a contiguous substring.
    E.g. 'ABC' is a subsequence of 'AXBYC' but not a substring.

    O(nm) or O(n^2) time complexity.

    Note: The Top Down Approach is more intuitive but may not be as fast.

    :param string_a: 1st string
    :param string_b: 2nd string
    :return: length of longest common subsequence
    """
    return


# ===================== Longest Palindromic Sequence =============================

# pprint import statement at top
# used to print matrices nicely
pp = pprint.PrettyPrinter()


def lps(input_string):
    """
    Find the most lengthy sequence of characters that is a palindrome in a single string.

    A palindrome is a string that reads the same backwards as forwards. E.g. 'MADAM'

    Time Complexity is O(n^2)

    Note: entire diagonal/bottom left of matrix will be 0 and answer will be in top, right cell

    Example:
        MAXDYAM, the LPS is MADAM, which has length = 5
        BANANO, the LPS is NAN, which has length = 3
        BxAoNxAoNxA, the LPS is ANANA, which has length = 5

    :param input_string: string
    :return: integer of length of largest palindrome
    """

    n = len(input_string)

    # create a lookup table to store results of subproblems
    table = [[0 for x in range(n)] for x in range(n)]

    # strings of length 1 have tablePS length = 1 (all diagonal cells in matrix)
    for i in range(n):
        table[i][i] = 1

    # consider all substrings
    for s_size in range(2, n + 1):  # 3

        for start_idx in range(n - s_size + 1):  # 1
            end_idx = start_idx + s_size - 1  # 3
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # match with a substring of length 2
                table[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]:
                # general match case
                table[start_idx][end_idx] = table[start_idx + 1][end_idx - 1] + 2
            else:
                # no match case, taking the max of either left cell or bottom cell
                table[start_idx][end_idx] = max(
                    # left cell
                    table[start_idx][end_idx - 1],
                    # bottom cell
                    table[start_idx + 1][end_idx])

    # pp.pprint(table)

    return table[0][n - 1]  # value in top right corner of matrix


print(lps('maxdyam'))
