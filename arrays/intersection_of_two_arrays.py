from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set = set(nums1)
        result = []

        for n in nums2:
            if n in hash_set:
                result.append(n)
                hash_set.remove(n)

        return result

# Time complexity: O(n + m) where n and m are the lengths of the input arrays
# Space complexity: O(n) where n is the length of the first input array

# Test cases

solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
assert solution.intersection(nums1, nums2) == [2], "Test case 1 failed"

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
assert solution.intersection(nums1, nums2) == [9, 4], "Test case 2 failed"

print("All test cases passed!")
