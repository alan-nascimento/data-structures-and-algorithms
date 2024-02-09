from typing import List
import os


def find_files(suffix: str, path: str) -> List[str]:
    files_with_suffix: List[str] = []

    def search_files(curr_path: str) -> None:
        if os.path.isfile(curr_path) and curr_path.endswith(suffix):
            files_with_suffix.append(curr_path)
        elif os.path.isdir(curr_path):
            for item in os.listdir(curr_path):
                search_files(os.path.join(curr_path, item))

    search_files(path)
    return files_with_suffix


# Test Cases
# Test Case 1: Basic test case
result = find_files('.c', './testdir')
expected = [
    './testdir/subdir3/subsubdir1/b.c',
    './testdir/t1.c',
    './testdir/subdir5/a.c',
    './testdir/subdir1/a.c',
]
assert result == expected

# Test Case 2: Edge case - empty directory
result = find_files('.c', './empty_dir')
expected = []
assert result == expected


# Test Case 3: Edge case - large directory
# Note: You need to create a large directory with .c files to test this case
result = find_files('.c', './testdir_large')
expected = [
    './testdir_large/subdir3/subsubdir1/b.c',
    './testdir_large/t1.c',
    './testdir_large/subdir5/a.c',
    './testdir_large/subdir6/a.c',
    './testdir_large/subdir6/subsubdir1/subsubsubdir1/t1.c',
    './testdir_large/subdir6/subsubdir1/subsubsubdir1/a.c',
    './testdir_large/subdir6/subsubdir1/a.c',
    './testdir_large/subdir1/a.c',
]
assert result == expected

print('All test cases passed successfully!')
