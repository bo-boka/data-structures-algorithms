
def sqrt(number):
    """
    Calculate the floored square root of a number with the expected time complexity of O(log(n))

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if type(number) != int:
        raise TypeError("The value entered is not a number.")
    if number == 0:
        return 0
    if number == 1:
        return 1

    def sqrt_recursive(sqr):

        same_num = number // sqr
        if same_num == sqr:
            return sqr

        return sqrt_recursive(sqr-1)

    start_num = number//2

    return sqrt_recursive(start_num)


print("Pass" if (3 == sqrt(9)) else "Fail")
# expected result "Pass"

print("Pass" if (0 == sqrt(0)) else "Fail")
# expected result "Pass"

print("Pass" if (4 == sqrt(16)) else "Fail")
# expected result "Pass"

print("Pass" if (1 == sqrt(1)) else "Fail")
# expected result "Pass"

print("Pass" if (5 == sqrt(27)) else "Fail")
# expected result "Pass"

print("Pass" if (5 == sqrt(25)) else "Fail")
# expected result "Pass"

try:
    print(sqrt("abcdefghijk"))
except TypeError as e:
    print(f'''{type(e).__name__}: {e}''')
# expected result TypeError

try:
    print(sqrt(False))
except TypeError as e:
    print(f'''{type(e).__name__}: {e}''')
# expected result TypeError

