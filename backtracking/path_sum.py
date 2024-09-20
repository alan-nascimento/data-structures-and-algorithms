from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currSum = 0) -> bool:
        if not root:
            return False

        currSum += root.val

        if not root.left and not root.right:
            return currSum == targetSum
        if self.hasPathSum(root.left, targetSum, currSum):
            return True
        if self.hasPathSum(root.right, targetSum, currSum):
            return True

        return False

# Time Complexity: O(N) where N is the number of nodes in the tree
# Space Complexity: O(H) where H is the height of the tree

# Test cases

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
assert (result := Solution().hasPathSum(root, 22)) == True, result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert (result := Solution().hasPathSum(root, 5)) == False, result

root = TreeNode(1)
root.left = TreeNode(2)
assert (result := Solution().hasPathSum(root, 0)) == False, result

print("Passed all test cases!")
