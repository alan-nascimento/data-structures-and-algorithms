from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                return [left + 1, right + 1]

# Time complexity: O(n) - where n is the length of the input list
# Space complexity: O(1) - no extra space is used

# Test cases

s = Solution()

# Test 1
assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]

# Test 2
assert s.twoSum([2, 3, 4], 6) == [1, 3]

# Test 3
assert s.twoSum([-1, 0], -1) == [1, 2]

# Test 4
assert s.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19) == [9, 10]

print("All tests passed!")
