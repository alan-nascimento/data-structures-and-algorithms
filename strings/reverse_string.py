from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        L, R = 0, len(s) - 1
        mid = len(s) // 2

        while L < mid:
            leftChar = s[L]

            s[L] = s[R]
            s[R] = leftChar

            L += 1
            R -= 1

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1)

# Test cases

solution = Solution()

s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
assert s == ["o", "l", "l", "e", "h"], "Test case 1 failed"

s = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s)
assert s == ["h", "a", "n", "n", "a", "H"], "Test case 2 failed"

print("All test cases passed!")
