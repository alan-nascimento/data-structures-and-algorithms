from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        self.inorderTraversal(root.left)
        self.arr.append(root.val)
        self.inorderTraversal(root.right)
        return self.arr

# Time Complexity: O(n) where n is the number of nodes in the binary tree
# Space Complexity: O(n) where n is the number of nodes in the binary tree

# Test cases

# Test 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
# Expected: [1, 3, 2]
r = Solution().inorderTraversal(root)
print(r)
assert r == [1, 3, 2]

# Test 2
root = TreeNode(1)
# Expected: [1]
r = Solution().inorderTraversal(root)
print(r)
assert r == [1]

# Test 3
root = TreeNode(1)
root.left = TreeNode(2)
# Expected: [2, 1]
r = Solution().inorderTraversal(root)
print(r)
assert r == [2, 1]

print("All tests passed!")
