

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        L = 0

        for R in range(1, len(intervals)):
            i1, i2 = intervals[L], intervals[R]

            if max(i1.start, i2.start) < min(i1.end, i2.end):
                return False
            else:
                L += 1

        return True

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1)

# Test cases

solution = Solution()

intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
assert solution.canAttendMeetings(intervals1) == False, "Test case 1 failed"

intervals2 = [Interval(7, 10), Interval(2, 4)]
assert solution.canAttendMeetings(intervals2) == True, "Test case 2 failed"

print("All test cases passed!")
