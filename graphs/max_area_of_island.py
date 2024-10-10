from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r, c - 1) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r + 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    max_area = max(max_area, curr_area)

        return max_area

# Time complexity: O(rows * cols) where rows is the number of rows and cols is the number of columns in the grid
# Space complexity: O(rows * cols) where rows is the number of rows and cols is the number of columns in the grid

# Test cases

s = Solution()

# Test 1
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0]
]
assert s.maxAreaOfIsland(grid) == 0

# Test 2
grid = [
    [1, 1, 0, 0, 0, 0, 0, 0]
]
assert s.maxAreaOfIsland(grid) == 2

# Test 3
grid = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
assert s.maxAreaOfIsland(grid) == 4
