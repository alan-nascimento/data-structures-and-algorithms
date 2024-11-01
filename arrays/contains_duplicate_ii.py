from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                hash_set.remove(nums[L])
                L += 1
            if nums[R] not in hash_set:
                hash_set.add(nums[R])
            else:
                return True

        return False

# Time Complexity: O(n) where n is the length of the input list
# Space Complexity: O(k) where k is the value of the input integer k

# Test Cases

solution = Solution()

assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3) == True
assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 4) == True

print("All test cases passed!")
