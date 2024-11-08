from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                intersections.append([start, end])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections

# Time complexity: O(n + m) where n and m are the lengths of the input arrays
# Space complexity: O(k) where k is the number of intersections

# Test cases

solution = Solution()

firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
assert solution.intervalIntersection(firstList, secondList) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]], "Test case 1 failed"

firstList = [[1, 3], [5, 9]]
secondList = []
assert solution.intervalIntersection(firstList, secondList) == [], "Test case 2 failed"

firstList = []
secondList = [[4, 8], [10, 12]]
assert solution.intervalIntersection(firstList, secondList) == [], "Test case 3 failed"

print("All test cases passed!")
