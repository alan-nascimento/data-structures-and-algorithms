from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root

# Time Complexity: O(H) where H is the height of the tree
# Space Complexity: O(H) where H is the height of the tree

# Test Cases

def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    solution = Solution()
    res = solution.insertIntoBST(root, 5)
    print(res.val)
    print(res.left.val)
    print(res.right.val)
    print(res.left.left.val)
    print(res.left.right.val)
    print(res.right.left)
    print(res.right.right)

if __name__ == '__main__':
    main()

print("All test cases passed!")
