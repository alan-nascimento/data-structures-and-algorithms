class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Iterate through all bits of the integer: O(k) where k is the number of bits in the integer
        # while n > 0:
        #     if n & 1 == 1:
        #         count += 1
        #     n = n >> 1

        # Optimized solution: O(p) where p is the number of 1 bits in the integer
        while n > 0:
            # n = n & (n - 1) # This operation removes the rightmost 1 bit
            n &= n - 1 # Simplified version of the above operation
            count += 1

        return count

# Time Complexity: O(p) where p is the number of 1 bits in the integer
# Space Complexity: O(1)

# Test Cases

solution = Solution()

assert solution.hammingWeight(11) == 3
assert solution.hammingWeight(128) == 1
assert solution.hammingWeight(4294967293) == 31

print("All test cases passed!")
