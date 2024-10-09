from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r + 1, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count

# Time complexity: O(m * n) where m is the number of rows and n is the number of columns
# Space complexity: O(m * n) where m is the number of rows and n is the number of columns

# Test Cases

islands = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
assert Solution().numIslands(islands) == 1

islands = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
assert Solution().numIslands(islands) == 3

print("All test cases passed!")
