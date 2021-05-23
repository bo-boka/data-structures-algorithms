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

    contents = os.listdir(path)
    for c in contents:
        new_path = os.path.join(path, c)
        if os.path.isdir(new_path):
            find_files(suffix, new_path)
        elif os.path.isfile(new_path) and c.endswith(suffix):
            print(c)


find_files(".c", "../../../Downloads/testdir/")
