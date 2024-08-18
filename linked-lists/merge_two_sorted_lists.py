from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next

# Time complexity: O(n + m) where n and m are the lengths of the two linked lists
# Space complexity: O(1) since no extra space is used

# Test cases
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
s = Solution()
assert s.mergeTwoLists(list1, list2) # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = None
assert s.mergeTwoLists(list1, list2).val == 1 # Output: 1 -> 2 -> 4

print("All test cases passed!")
