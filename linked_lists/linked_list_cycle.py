from typing import Optional

class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head.next

        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        return False

# Time Complexity: O(n) where n is the length of the linked list
# Space Complexity: O(1)

# Test Cases:

solution = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next = head
assert solution.hasCycle(head) == True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
assert solution.hasCycle(head) == False

assert solution.hasCycle(None) == False

print("All test cases passed!")
