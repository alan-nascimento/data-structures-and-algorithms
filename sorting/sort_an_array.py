from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid_index = len(nums) // 2

        left = self.sortArray(nums[0:mid_index])
        right = self.sortArray(nums[mid_index:])

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []

        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result

# Merge sort solution

# Time complexity: O(n log n) where n is the length of the input list
# Space complexity: O(n) because we are using extra space to store the sorted list

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
