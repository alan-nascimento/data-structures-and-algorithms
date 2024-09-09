from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = None
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = top + (bot - top) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                row = matrix[mid]
                break

        if not row:
            return False

        left, right = 0, len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# Time Complexity: O(log(m) + log(n)) where m is the number of rows and n is the number of columns
# Space Complexity: O(1) as we are not using any extra space

# Test cases
tests = [
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True],
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False],
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0, False],
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61, False],
]

solver = Solution()

for test in tests:
    assert solver.searchMatrix(test[0], test[1]) == test[2]

print("All tests passed!")
