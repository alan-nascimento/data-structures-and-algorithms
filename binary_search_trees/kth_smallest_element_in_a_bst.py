from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)
        return self.arr[k - 1]

    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)

        return root

# Time Complexity: O(n) where n is the number of nodes in the binary tree
# Space Complexity: O(n) where n is the number of nodes in the binary tree

# Test cases

# Test 1
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
# Expected: 1
r = Solution().kthSmallest(root, 1)
print(r)
assert r == 1

# Test 2
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
# Expected: 3
r = Solution().kthSmallest(root, 3)
print(r)
assert r == 3

print("All tests passed!")
