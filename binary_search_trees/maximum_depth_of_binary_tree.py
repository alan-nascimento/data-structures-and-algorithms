from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth

# Time complexity: O(n) where n is the number of nodes in the binary tree
# Space complexity: O(n) where n is the number of nodes in the binary tree

# Test cases

solution = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

assert solution.maxDepth(root) == 3, "Test case 1 failed"

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

assert solution.maxDepth(root) == 3, "Test case 2 failed"

print("All test cases passed!")
