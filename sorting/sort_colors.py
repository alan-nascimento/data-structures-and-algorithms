from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            swapped = True
            for j in range(1, n):
                prev = nums[j - 1]
                curr = nums[j]
                if prev > curr:
                    nums[j], nums[j - 1] = prev, curr
                    swapped = False
            if swapped:
                break

# Bubble sort solution

# Time complexity: O(n^2) where n is the number of elements in nums
# Space complexity: O(1) because we are not using any extra space

# Test cases

# Test case 1
nums = [2, 0, 2, 1, 1, 0]
# Output
# [0, 0, 1, 1, 2, 2]
r = Solution().sortColors(nums)
assert nums == [0, 0, 1, 1, 2, 2]

# Test case 2
nums = [2, 0, 1]
# Output
# [0, 1, 2]
r = Solution().sortColors(nums)
assert nums == [0, 1, 2]

# Test case 3
nums = [0]
# Output
# [0]
r = Solution().sortColors(nums)
assert nums == [0]
