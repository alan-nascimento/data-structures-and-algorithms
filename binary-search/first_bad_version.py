def isBadVersion(version: int) -> bool:
    if version == 4:
        return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Time complexity: O(log n) - Binary search
# Space complexity: O(1) - Constant space

# Test cases

# Test 1
# n = 5
# isBadVersion = 4
# Expected output = 4
s = Solution().firstBadVersion(5)
assert s == 4, f"Expected output: 4, but got {s}"

# Test 2
# n = 1
# isBadVersion = 1
# Expected output = 1
s = Solution().firstBadVersion(1)
assert s == 1, f"Expected output: 1, but got {s}"
