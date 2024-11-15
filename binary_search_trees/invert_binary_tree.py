
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])

        while q:
            levels = len(q)

            for _ in range(levels):
                curr = q.popleft()

                temp = curr.left
                curr.left = curr.right
                curr.right = temp

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root

# Time complexity: O(n) where n is the number of nodes in the binary tree, since we are visiting each node once
# Space complexity: O(n) where n is the number of nodes in the binary tree, since we are using a queue to store the nodes

# Test cases

solution = Solution()

# Test 1
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
# Expected: 4, 7, 2, 9, 6, 3, 1
r = solution.invertTree(root)
assert r.val == 4
assert r.left.val == 7
assert r.right.val == 2
assert r.left.left.val == 9
assert r.left.right.val == 6
assert r.right.left.val == 3
assert r.right.right.val == 1

# Test 2
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# Expected: 2, 3, 1
r = solution.invertTree(root)
assert r.val == 2
assert r.left.val == 3
assert r.right.val == 1

print("All test cases passed!")
