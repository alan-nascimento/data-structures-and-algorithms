from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            level = []

            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.append(level)

        return result

# Time complexity: O(n) where n is the number of nodes in the binary tree.
# Space complexity: O(n) where n is the number of nodes in the binary tree.

# Test cases

# Test 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# Output: [[3], [9, 20], [15, 7]]
print(Solution().levelOrder(root))
assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]

# Test 2

# Output: []
print(Solution().levelOrder(None))
assert Solution().levelOrder(None) == []

# Test 3
root = TreeNode(1)
# Output: [[1]]
print(Solution().levelOrder(root))
assert Solution().levelOrder(root) == [[1]]

# Test 4
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# Output: [[1], [2, 5], [3, 4, 6, 7]]
print(Solution().levelOrder(root))
assert Solution().levelOrder(root) == [[1], [2, 5], [3, 4, 6, 7]]

print("All test cases passed!")
