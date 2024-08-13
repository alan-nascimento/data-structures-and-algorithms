class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')': '(', '}': '{', ']': '[' }
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

# Time Complexity: O(n) where n is the length of the input string
# Space Complexity: O(n) where n is the length of the input string

# Test Cases

assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False
assert Solution().isValid("({[]})") == True

print("All test cases passed!")
