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

def lcs_memoization(str_a, str_b):
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

    def lcs(a, b):

        if a == 0 or b == 0:
            return 0

        # If we have already computed this, use memoization
        if cache[a - 1][b - 1] != -1:
            return cache[a - 1][b - 1]

        a_last_char = str_a[a - 1]
        b_last_char = str_b[b - 1]

        if a_last_char == b_last_char:
            cache[a - 1][b - 1] = 1 + lcs(a - 1, b - 1)
        else:
            cache[a - 1][b - 1] = max(lcs(a - 1, b), lcs(a, b - 1))

        return cache[a - 1][b - 1]

    # Initialise a 2D array with NULL
    cache = [[-1 for j in range(len(str_b))] for i in range(len(str_a))]
    return lcs(len(str_a), len(str_b))

'''
# Tests
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs_memoization(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs_memoization(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')
'''


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
    for s_size in range(2, n + 1):  # 2

        for start_idx in range(n - s_size + 1):  # 4
            end_idx = start_idx + s_size - 1  # 5
            # note: not seeing why this case is added since it's still covered in the general match case below (the diagonal/bottom-left will be 0 so you're still just adding 2 to 0)
            if s_size == 2 and input_string[start_idx] == input_string[end_idx]:
                # matching letters are next to each other: match with a substring of length 2
                table[start_idx][end_idx] = 2
            elif input_string[start_idx] == input_string[end_idx]:
                # general match case: assign diagonal/bottom-left plus 2
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


# print(lps('maxdyam'))


# ===================== Coin Change Problem - TDA =============================

def coin_change_memoization(coins, amount):
    """
    You are given coins of different denominations and a total amount of money. Write a function to compute the fewest
    coins needed to make up that amount using a top-down approach.
    If that amount of money cannot be made up by any combination of the coins, return -1.

    Note: A greedy approach, where we choose the largest coin amounts first would not work because we could end up with
          a large coin and a bunch of small ones. E.g. if amt = 7, coins = [1,3,4,5] a greedy approach would have us
          choose [5,1,1] instead of [4,3]

    Logic: Let's assume F(Amount) is the minimum number of coins needed to make a change from coins [C0, C1, C2...Cn-1]
           Then, we know that F(Amount) = min(F(Amount-C0), F(Amount-C1), F(Amount-C2)...F(Amount-Cn-1)) + 1

    Time Complexity: O(Nm) where N is the amount and m is the len of coins
    Space Complexity: O(n)

    As an example:
        Input: coins = [1, 2, 3], amount = 6
        Output: 2
        Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use
        3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should
        use the smallest number of coins possible.

    :param coins: list of integers representing coin values
    :param amount: integer representing amount of money
    :return: integer of fewest coins needed to reach the given amount
    """

    memo = {}  # store calculated values to avoid recomputation

    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0

        # Check if we have already calculated
        if remaining not in memo:
            # calculate & store for each amount.
            # +1 for each -c because we're adding a coin to the count when we subtract it's value from amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]

    res = return_change(amount)
    print(memo)
    # return -1 when no change found
    return -1 if res == float('inf') else res


'''
# Tests
print(coin_change_memoization([1, 2, 5], 11))  # expected 3
print(coin_change_memoization([1, 4, 5, 6], 23))  # expected 4
print(coin_change_memoization([5, 7, 8], 2))  # expected -1
'''


# ===================== Coin Change Problem - BUA =============================

def coin_change_tabulation(coins, amount):
    """
    You are given coins of different denominations and a total amount of money. Write a function to compute the fewest
    coins needed to make up that amount using a bottom-up approach.
    If that amount of money cannot be made up by any combination of the coins, return -1.

    Note: A greedy approach, where we choose the largest coin amounts first would not work because we could end up with
          a large coin and a bunch of small ones. E.g. if amt = 7, coins = [1,3,4,5] a greedy approach would have us
          choose [5,1,1] instead of [4,3]

    Time Complexity: O(Nm) where N is the amount and m is the len of coins
    Space Complexity: O(n)

    As an example:
        Input: coins = [1, 2, 3], amount = 6
        Output: 2
        Explanation: The output is 2 because we can use 2 coins with value 3. That is, 6 = 3 + 3. We could also use
        3 coins with value 2 (that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem specifies we should
        use the smallest number of coins possible.

    :param coins: list of integers representing coin values
    :param amount: integer representing amount of money
    :return: integer of fewest coins needed to reach the given amount
    """

    # initiate the list with length amount + 1 and prefill with the max value
    table = [amount + 1] * (amount + 1)  # can also use float('inf') but we know that max is anything over the amount

    # when amount = 0, 0 number of coins will be needed for the change
    table[0] = 0

    for a in range(1, amount + 1):  # 'a' represents the smaller problem to solve, starting from bottom up (1...)
        for c in coins:

            # if current amount, a, minus a coin value, c, doesn't go below 0,
            # we can still find a solution for the table, even if it's not the most optimal
            if a - c >= 0:
                # set to min between current solution (itself) or new solution (itself minus another coin)
                # +1 because we add a coin to the solution every time we subtract a coin value from the amount
                table[a] = min(table[a], 1 + table[a-c])  # this is the recurrence relation

    return table[amount] if table[amount] != amount + 1 else -1


'''
# Tests
print(coin_change_tabulation([1, 2, 5], 11))  # expected 3
print(coin_change_tabulation([1, 4, 5, 6], 23))  # expected 4
print(coin_change_tabulation([5, 7, 8], 2))  # expected -1
'''


# ===================== Max Stock Price Returns =============================

def max_returns(prices):
    """
    You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the
    stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a
    function that returns the maximum profit obtainable. You will need to buy before you can sell.

    Consider time complexity in solution

    Example:
        prices = [3, 4, 7, 8, 6]
            Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have
            13 elements (one price for each 30 minute interval between 9:30 and 4:00), as seen in the test cases.
        Solution: 5
        Explanation: In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell
        at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible
        difference between two numbers in the array such that the smaller number is sequentially first.

    The Idea:

        The given array has the prices of a single stock at 13 different timestamps. The idea is to pick two timestamps:
        "buy_at_min" and "sell_at_max" such that the buy is made before a sell. We will use two pairs of indices while
        traversing the array:
            Pair 1 - This pair keeps track of our maximum profit while iterating over the list. It is done by storing a
                pair of indices - min_price_index, and max_price_index.
            Pair 2 - This pair keeps track of the profit between the lowest price seen so far and the current price
                while traversing the array. The lowest price seen so far is maintained with current_min_price_index.
        At each step we will make the greedy choice by choosing prices such that our profit is maximum.
        We will store the maximum of either of the two profits mentioned above.

    Args:
       prices: array of prices
    Returns:
       int: The maximum profit possible
    """

    if len(prices) < 2:
        return None  # (should throw exception)

    min_idx = 0
    max_idx = 1
    temp_min = 0

    for i in range(1, len(prices)):

        # set temporary min until you find a new max so that min doesn't pass max
        if prices[i] < prices[temp_min]:
            temp_min = i

        # when new max profit found, set max & min
        if prices[max_idx] - prices[min_idx] < prices[i] - prices[temp_min]:
            max_idx = i
            min_idx = temp_min

    return prices[max_idx] - prices[min_idx]


# Tests
print(max_returns([2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]))  # expected 76
print(max_returns([54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]))  # expected 66
print(max_returns([78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]))  # expected 0


