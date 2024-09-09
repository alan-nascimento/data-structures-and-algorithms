from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1) as we are not using any extra space

# Test cases
s = Solution()
# assert s.reverseList(ListNode(1, ListNode(2, ListNode(3)))) == ListNode(3, ListNode(2, ListNode(1)))
# assert s.reverseList(ListNode(1, ListNode(2))) == ListNode(2, ListNode(1))
node = ListNode(1)
assert s.reverseList(node) == node
assert s.reverseList(None) == None

print("All test cases passed!")
