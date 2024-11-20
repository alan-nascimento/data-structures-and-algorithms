from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_element = min(nums[left], nums[right])

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < min_element:
                right = mid - 1
                min_element = nums[mid]
            else:
                left = mid + 1

        return min_element

# Time Complexity: O(log n) where n is the number of elements in nums
# Space Complexity: O(1) since we are not using any additional space

# Test Cases:

solution = Solution()
assert solution.findMin([3, 4, 5, 1, 2]) == 1
assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert solution.findMin([11, 13, 15, 17]) == 11

print("All test cases passed!")
