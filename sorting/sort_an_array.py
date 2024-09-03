from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid_index = len(nums) // 2

        left = self.sortArray(nums[0:mid_index])
        right = self.sortArray(nums[mid_index:])

        return self.merge(left, right)

    def merge(self, left, right):
        arr = []

        while left and right:
            if left < right:
                arr.append(left)
            else:
                arr.append(right)

        return arr

# Time complexity: O(nlogn) where n is the length of the input list
# Space complexity: O(n) where n is the length of the input list

# Test cases

s = Solution()
r = s.sortArray([5,2,3,1])
assert r == [1,2,3,5]
print(r) # [1,2,3,5]

r = s.sortArray([5,1,1,2,0,0])
assert r == [0,0,1,1,2,5]
print(r) # [0,0,1,1,2,5]

r = s.sortArray([1,2,3,4,5])
assert r == [1,2,3,4,5]
print(r) # [1,2,3,4,5]

print("All test cases passed!")
