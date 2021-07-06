import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Cannot use the Python method os.walk()

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    try:
        contents = os.listdir(path)
        for c in contents:
            new_path = os.path.join(path, c)
            if os.path.isdir(new_path):
                find_files(suffix, new_path)
            elif os.path.isfile(new_path) and c.endswith(suffix):
                print(c)
    except Exception as e:
        print(e)


# Test case 1
print('======== Test 1: Happy Path')
find_files(".c", "../../../Downloads/testdir/")     # prints all files ending in .c from all dir and sub-dir

# Test case 2
print('======== Test 2: File is empty string')
find_files("", "../../../Downloads/testdir/")       # prints all files

# Test case 3
print('======== Test 3: No directory specified')
find_files(".c", "")                                # raises missing file/directory error

# Test case 4
print('======== Test 4: Invalid input path')
find_files(".c", "1234")                            # raises missing file/directory error

# Test case 5
print('======== Test 5: No files found')
find_files(".abc", "../../../Downloads/testdir")    # prints nothing
