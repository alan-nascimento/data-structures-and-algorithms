from typing import List

class Solution:
  def findMaxSumSubArray(self, k: int, arr: List[int]) -> int:
    max_index = len(arr) - k
    max_sum = -1
    i = 0

    while i <= max_index:
      curr_sum = 0

      for j in range(i, i + k):
        curr_sum += arr[j]

      max_sum = max(max_sum, curr_sum)
      i += 1

    return max_sum

# Time complexity: O(N * K)
# Space complexity: O(1)

# Test cases

s = Solution()

print(s.findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2])) # 9
assert s.findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2]) == 9

print(s.findMaxSumSubArray(2, [2, 3, 4, 1, 5])) # 7
assert s.findMaxSumSubArray(2, [2, 3, 4, 1, 5]) == 7

print(s.findMaxSumSubArray(3, [2, 1, 5, 2, 3, 2])) # 10
assert s.findMaxSumSubArray(3, [2, 1, 5, 2, 3, 2]) == 10

print("All test cases pass")
