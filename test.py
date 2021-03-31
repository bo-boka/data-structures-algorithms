
def test_function(attempt, expected_result, func):
    """
    Function to test other functions
    First prints actual result
    Only takes 1 attempt input so will not work with a function with multiple inputs
    Different data type inputs are commented out
        TODO: add checks for data types
    :param attempt: input of function to be tested
    :param expected_result: expected result
    :param func: function to be tested
    :return: throws an Assertion Error with details if fail, nothing if pass
    """
    print('Actual Result from attempt: {}'.format(func(attempt)))

    # attempt is int, result is list
    # assert func(attempt) == expected_result, str(attempt) + " should be [" + ', '.join(expected_result) + "]"

    # attempt is list of ints, result is list of lists of ints
    # assert func(attempt) == expected_result, "[" + ', '.join(map(str, attempt))+"] should be [" + ', '.join(map(str, expected_result)) + "]"

    # attempt is int, result is int
    assert func(attempt) == expected_result, str(attempt) + " should be " + str(expected_result)
    print("Pass")


if __name__ == "__main__":
    test_function()
    print('everything passed')