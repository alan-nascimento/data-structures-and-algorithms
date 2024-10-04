from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        counts = []
 
        def dfs(curr, counter = 0):
            if not curr:
                return None

            counter += 1

            if not curr.left and not curr.right:
                counts.append(counter)
                counter = 0
                return None

            dfs(curr.left, counter)
            dfs(curr.right, counter)

            return curr
        
        dfs(root)

        return min(counts) if counts else 0

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) where n is the number of nodes in the tree

# Test Cases

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
assert Solution().minDepth(root) == 2

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
assert Solution().minDepth(root) == 5

print("All test cases passed!")
