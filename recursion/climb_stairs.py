class Solution:
    def climbStairs(self, n: int) -> int:
        hash_map = {}

        def climb(step):
            if step > n:
                return 0

            if step == n:
                return 1

            if step in hash_map:
                return hash_map[step]

            hash_map[step] = climb(step + 1) + climb(step + 2)

            return hash_map[step]

        return climb(1) + climb(2)

# Time Complexity: O(n) where n is the number of steps, since we are memoizing the results
# Space Complexity: O(n) where n is the number of steps, for the hash map

# Test cases

s = Solution()

# Test 1
# 2 steps
# 1 + 1
# 2
assert s.climbStairs(2) == 2

# Test 2
# 3 steps
# 1 + 1 + 1
# 1 + 2
# 2 + 1
# 3
assert s.climbStairs(3) == 3

# Test 3
# 38 steps
assert s.climbStairs(38) == 63245986

print("All tests passed!")
