from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])

        merge = []

        for i in range(len(intervals)):
            if not merge or merge[-1][1] < intervals[i][0]:
                merge.append(intervals[i])
            else:
                merge[-1][1] = max(merge[-1][1], intervals[i][1])

        return merge

# Time Complexity: O(n) where n is the length of the intervals list
# Space Complexity: O(k) where k is the number of merged intervals

# Test Cases

s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
assert s.merge(intervals) == [[1,6],[8,10],[15,18]], "Test case 1 failed"

intervals = [[1,4],[4,5]]
assert s.merge(intervals) == [[1,5]], "Test case 2 failed"

intervals = [[1,4],[0,4]]
assert s.merge(intervals) == [[0,4]], "Test case 3 failed"

print("All test cases passed!")
