from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# Time complexity: O(log n) where n is the number of elements in the list
# Space complexity: O(1) since we are using only a constant amount of space

# Test cases

# Test case 1
# The target is 9 and it is present in the list at index 3
r = Solution().search([-1, 0, 3, 9, 12], 9)
assert r == 3

# Test case 2
# The target is 2 and it is not present in the list
r = Solution().search([-1, 0, 3, 9, 12], 2)
assert r == -1

# Test case 3
# The list is empty
r = Solution().search([], 5)
assert r == -1

print("All test cases passed!")
