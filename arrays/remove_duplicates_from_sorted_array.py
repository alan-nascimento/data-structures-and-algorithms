from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1) as we are not using any extra space

# Test cases
s = Solution()
assert s.removeDuplicates([1, 1, 2]) == 2
assert s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert s.removeDuplicates([1, 2, 3]) == 3
assert s.removeDuplicates([1, 1, 1]) == 1

print("All test cases passed!")
