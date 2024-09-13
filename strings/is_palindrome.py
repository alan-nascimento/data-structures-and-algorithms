class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True

# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(1) since we are not using any extra space

# Test Cases

r = Solution().isPalindrome("A man, a plan, a canal: Panama")
assert r == True

r = Solution().isPalindrome("race a car")
assert r == False

r = Solution().isPalindrome("Marge, let's \"[went].\" I await {news} telegram.")
assert r == True
