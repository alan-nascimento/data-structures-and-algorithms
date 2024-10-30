from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(currSum, 0)
            currSum += n
            maxSum = max(maxSum, currSum)

        return maxSum

# Time complexity: 𝑂(𝑛) where n is the number of elements in the array
# Space complexity: 𝑂(1)

# Test cases

solution = Solution()

assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert solution.maxSubArray([1]) == 1
assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
assert solution.maxSubArray([-1]) == -1
assert solution.maxSubArray([-2, 1]) == 1

print("All test cases passed!")
