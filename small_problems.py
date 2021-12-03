def add_one(arr):
    """
    desc: add one to a number represented as a list. Solve without converting to a number.
    param: arr - list of digits representing some number x
    return: a list with digits represengint (x + 1)
    """

    arr_len = len(arr)
    if arr_len == 0:
        return None
    # to traverse an array in reverse, use range as so and -1 from i
    for i in range(arr_len, 0, -1):
        print(arr[i-1])
        if arr[i-1] == 9:
            arr[i-1] = 0
            if i-1 == 0:
                # prepend to array
                arr = [1] + arr
                return arr
        else:
            arr[i-1] = arr[i-1] +1
            return arr
    return arr


def duplicate_number(arr):
    """
    param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    if len(arr) == 0:
        return None
    dup_arr = []
    for num in arr:
        if num in dup_arr:
            return num
        else:
            dup_arr.append(num)
    return None


def max_sum_subarray(arr):
    """
    desc - finds max sum of contiguous values without using nested loop
    param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """

    current_sum = arr[0]  # `current_sum` denotes the sum of a subarray
    max_sum = arr[0]  # `max_sum` denotes the maximum value of `current_sum` ever

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)

        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)

    return max_sum


def nth_row_pascal(n):
    """
    Return a list of nth row of Pascal's Triangle.

    Pascal's Triangle is a triangle with where the first row (& triangle top) is a unique non-zero entry of 1.
    Each subsequent row is formed by adding the top-left & top-right number's together.

    param - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    pasc_arr = [[1]]
    for i in range(n):
        new_row = [1]
        pasc_row = pasc_arr[-1]
        for j in range(1, len(pasc_row)):
            new_row.append(pasc_row[j] + pasc_row[j-1])
        new_row.append(1)
        pasc_arr.append(new_row)

    return pasc_arr[n]


def time_conversion(s):
    """
    Convert am/pm time to military time
    :param s: string formatted hh:mm:ssA
    :return:
    """

    # can also use datetime module
    # from datetime import *
    # ampm_time = datetime.strptime(s, "%I:%M:%S%p")
    # return datetime.strftime(ampm_time, "%H:%M:%S")

    meridiem = s[-2:].upper()
    mins_secs = s[2:-2]
    hour = int(s[:2])

    hour = hour % 12 if meridiem == 'AM' else hour % 12 + 12
    # can add leading 0 using format
    return f'{hour:02}{mins_secs}'


# print(timeConversion('04:01:23PM'))


def diagonal_difference(arr):
    """
    Given a square matrix, find the absolute value of it's two diagonal sums.
    :param arr: nested list; square matrix
    :return: absolute value of sum differences
    """
    a_len = len(arr)
    top_d, bottom_d = 0, 0

    for i in range(a_len):
        top_d += arr[i][i]
        bottom_d += arr[a_len - 1 - i][i]

    return abs(top_d - bottom_d)


def palindromic_count(my_str):
    """
    return palindromic count of strings (# of non palindromic matches)
    :param my_str:
    :return:
    """

    count = 0

    for i in range(len(my_str)//2):
        print('front', my_str[i], '--back', my_str[-i-1])
        if my_str[i] != my_str[-i-1]:
            count += 2

    return count


# my_str = 'fox'
# my_str = 'abba'
# my_str = 'malayalam'
# print('palindromic count', palindromic_count(my_str))

def find_misplaced_sequence(arr):
    """
    Given an array of numbers that, if sorted, are in succession, find the duplicate number.
    Return duplicate & missing number in tuple.

    Examples:
        [2,2,3,4] --> (2,1)
        [4,3,1,3,5] --> (3,2)
        [6,7,5,3,5] --> (5,4)

    :param arr: array of ints
    :return: tuple of duplicate & missing number
    """

    sorted_nums = arr.sort()
    print(sorted_nums)
    offset = sorted_nums[0]
    duplicate = 0
    missing = 0

    for i in range(1, len(arr)):
        should_num = i + offset
        if arr[i] != should_num:
            duplicate = arr[i]
            if arr[i-1] == arr[i]:
                # if the out of place duplicate is second, the missing number is in sequence before it
                missing = duplicate + 1
            else:
                # if the out of place duplicate is first, the missing number is in sequence after it
                missing = duplicate - 1

        return duplicate, missing


seq = [2,2,3,4]  # (2,1)
# seq = [4,3,1,3,5]  # (3,2)
# seq = [6,7,5,3,5]  # (5,4)
print('dup_seq', find_misplaced_sequence(seq))

