class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)

# Time complexity: O(n)
# Space complexity: O(n)

# Test cases

s = Solution()

# Test
assert s.simplifyPath("/home/") == "/home"

# Test 2
assert s.simplifyPath("/../") == "/"

# Test 3
assert s.simplifyPath("/home//foo/") == "/home/foo"

# Test 4
assert s.simplifyPath("/a/./b/../../c/") == "/c"

# Test 5
assert s.simplifyPath("/a/../../b/../c//.//") == "/c"

# Test 6
assert s.simplifyPath("/a//b////c/d//././/..") == "/a/b/c"

print("All tests passed!")
