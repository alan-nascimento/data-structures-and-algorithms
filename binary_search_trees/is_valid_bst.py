from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def dfs(curr: Optional[TreeNode]) -> None:
            if not curr:
                return curr

            dfs(curr.left)
            inorder.append(curr.val)
            dfs(curr.right)

        dfs(root)

        for i in range(1, len(inorder)):
            if inorder[i - 1] >= inorder[i]:
                return False

        return True

# Time Complexity: O(n) where n the number of nodes in the tree
# Space Complexity: O(n) where n is the number of nodes in the tree

# Test Cases

solution = Solution()

# [2, 1, 3]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert solution.isValidBST(root) == True

# [5,1,4,null,null,3,6]
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
assert solution.isValidBST(root) == False

print("All test cases passed!")
