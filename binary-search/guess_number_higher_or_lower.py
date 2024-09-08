def guess(num: int) -> int:
    pick = 6

    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n

        while low <= high:
            mid = low + (high - low) // 2

            if guess(mid) < 0:
                high = mid - 1
            elif guess(mid) > 0:
                low = mid + 1
            else:
                return mid

        return -1

# Time complexity: O(log n) - Binary search
# Space complexity: O(1) - Constant space

# Test cases

# 1
solution = Solution()
assert solution.guessNumber(10) == 6

# 2
solution = Solution()
assert solution.guessNumber(1) == -1

# 3
solution = Solution()
assert solution.guessNumber(100) == 6

print("All test cases pass")
