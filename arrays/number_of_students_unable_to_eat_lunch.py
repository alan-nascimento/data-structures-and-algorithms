from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = { 0: 0, 1: 0 }

        for i in students:
            count[i] += 1

        for j in sandwiches:
            if count[j] > 0:
                count[j] -= 1
            else:
                break

        return count[0] + count[1]

# Time Complexity: O(n) where n is the length of the students array
# Space Complexity: O(1) since the count dictionary will always have 2 keys

# Test cases

s = Solution()

# Test 1

students = [1,1,0,0]
sandwiches = [0,1,0,1]
assert s.countStudents(students, sandwiches) == 0

# Test 2

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
assert s.countStudents(students, sandwiches) == 3

print("All tests passed!")
