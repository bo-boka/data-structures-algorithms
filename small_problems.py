def add_one(arr):
    """
    desc: add one to a number represented as a list. Solve without converting to a number.
    param: arr - list of digits representing some number x
    return: a list with digits represengint (x + 1)
    """

    arr_len = len(arr)
    if arr_len == 0:
        return None
    #to traverse an array in reverse, use range as so and -1 from i
    for i in range(arr_len, 0, -1):
        print(arr[i-1])
        if (arr[i-1] == 9):
            arr[i-1] = 0
            if (i-1 == 0):
                #prepend to array
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
    desc - finds max sum of contiguous values vals without using nested loop
    param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """

    def max_sum_subarray(arr):

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

print(nth_row_pascal(4))

