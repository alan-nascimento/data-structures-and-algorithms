from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                minNode = self.minNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, root.val)

        return root

    def minNode(self, curr: TreeNode) -> TreeNode:
        while curr and curr.left:
           curr = curr.left
        return curr

# Time Complexity: O(H), where H is the height of the tree
# Space Complexity: O(1) since we are not using any extra space

# Test cases

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
key = 3

# Expected: 5
assert Solution().deleteNode(root, key).val == 5

print("All test cases passed!")
