class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        reverse_index = len(s) - 1

        for index in range(len(s) - 1):
            if s[index] != s[reverse_index]:
                return False
            reverse_index -= 1

        return True

# Time complexity: O(n) where n is the number of digits in x
# Space complexity: O(1) because we are not using any extra space

# Test cases

# Test case 1

# Input
x = 121
# Output
# True
r = Solution().isPalindrome(x)
print(r)
assert r == True

# Test case 2
x = -121
# Output
# False
r = Solution().isPalindrome(x)
print(r)
assert r == False

# Test case 3
x = 10
# Output
# False
r = Solution().isPalindrome(x)
print(r)
assert r == False

print("All test cases pass")
