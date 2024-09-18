from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []

        if root:
            queue.append(root)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                if i == 0:
                    result.append(curr.val)

        return result

# Time complexity: O(n) where n is the number of nodes in the binary tree.
# Space complexity: O(n) where n is the number of nodes in the binary tree.

# Test cases

# Test 1
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
# Output: [1, 3, 4]
print(Solution().rightSideView(root))
assert Solution().rightSideView(root) == [1, 3, 4]

# Test 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)
# Output: [1, 3, 6, 8]
print(Solution().rightSideView(root))
assert Solution().rightSideView(root) == [1, 3, 6, 8]

print("All test cases passed!")
