from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        def revert(prev_node, curr_node, next_node):
            if next_node is None:
                return curr_node

            next_node_ref = next_node.next

            curr_node.next = prev_node
            next_node.next = curr_node

            return revert(curr_node, next_node, next_node_ref)

        return revert(None, head, head.next)

# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(n) where n is the number of nodes in the linked list

# Test cases

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()

# Expected: 5 -> 4 -> 3 -> 2 -> 1
reversed_head = solution.reverseList(head)

assert reversed_head.val == 5

while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
