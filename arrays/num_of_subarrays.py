from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        count = 0
        curr_sum = 0

        for R in range(len(arr)):
            curr_sum += arr[R]
            if R - L == k - 1:
                if curr_sum // k >= threshold:
                    count += 1
                curr_sum -= arr[L]
                L += 1

        return count

# Time Complexity: O(n) where n is the length of the input list
# Space Complexity: O(1) since we are using a constant amount of space

# Test Cases

solution = Solution()

assert solution.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
assert solution.numOfSubarrays([1, 1, 1, 1, 1], 1, 0) == 5
assert solution.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6

print("All test cases passed!")
