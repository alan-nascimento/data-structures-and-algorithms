import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h, self.k = nums, k
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]

# Time Complexity: O(n log k) for initialization, O(log k) for add
# Space Complexity: O(k) for initialization, O(1) for add

# Test cases

kth_largest = KthLargest(3, [4, 5, 8, 2])
assert kth_largest.add(3) == 4
assert kth_largest.add(5) == 5
assert kth_largest.add(10) == 5
assert kth_largest.add(9) == 8
assert kth_largest.add(4) == 8

kth_largest = KthLargest(1, [])
assert kth_largest.add(-3) == -3
assert kth_largest.add(-2) == -2
assert kth_largest.add(-4) == -2

print("All test cases passed!")
