from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.stack = []

    def next(self) -> int:
        while self.hasNext():
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                prev = self.stack.pop()
                self.curr = prev.right
                return prev.val

    def hasNext(self) -> bool:
        return self.curr is not None or len(self.stack) > 0

# Time complexity: O(n) where n is the number of nodes in the binary search tree
# Space complexity: O(h) where h is the height of the binary search tree

# Test cases

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root)
assert iterator.next() == 3
assert iterator.hasNext() == True
assert iterator.next() == 7
assert iterator.hasNext() == True
assert iterator.next() == 9
assert iterator.hasNext() == True
assert iterator.next() == 15
assert iterator.hasNext() == True
assert iterator.next() == 20
assert iterator.hasNext() == False

print("All test cases passed!")
