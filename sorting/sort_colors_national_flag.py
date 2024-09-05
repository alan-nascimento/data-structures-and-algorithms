from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Dutch National Flag problem solution

# Time complexity: O(n) where n is the number of elements in nums
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

print("All tests passed.")
