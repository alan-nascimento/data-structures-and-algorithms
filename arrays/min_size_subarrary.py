from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, total = 0, 0
        length = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L = L + 1

        return 0 if length == float("inf") else length

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1)

# Test cases

solution = Solution()

nums1 = [2, 3, 1, 2, 4, 3]
target1 = 7
assert solution.minSubArrayLen(target1, nums1) == 2, "Test case 1 failed"

nums2 = [1, 4, 4]
target2 = 4
assert solution.minSubArrayLen(target2, nums2) == 1, "Test case 2 failed"

nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
target3 = 11
assert solution.minSubArrayLen(target3, nums3) == 0, "Test case 3 failed"

print("All test cases passed!")
