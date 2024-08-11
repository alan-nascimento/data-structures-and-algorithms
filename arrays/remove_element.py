from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1) as we are not using any extra space

# Test cases
s = Solution()
assert s.removeElement([3, 2, 2, 3], 3) == 2
assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
assert s.removeElement([1, 2, 3], 4) == 3
assert s.removeElement([1, 1, 1], 1) == 0

print("All test cases passed!")
