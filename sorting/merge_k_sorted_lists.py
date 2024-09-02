from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = None
        tail = None

        for i in range(len(lists)):
            if not head:
                head = lists[i]
            elif tail:
                tail.next = lists[i]

            curr = head if not tail else tail
            while curr:
                if not curr.next:
                    tail = curr
                curr = curr.next

        if not head:
            return None

        iterator = head
        prev = head
        curr = head.next

        while iterator:
            if curr and prev and prev.val > curr.val:
                temp = prev.val
                prev.val = curr.val
                curr.val = temp

            if not curr:
                prev = head
                curr = head.next
                iterator = iterator.next
            else:
                prev = prev.next
                curr = curr.next

        return head


# Time complexity: O(n^2) where n is the total number of nodes in the k linked lists
# Space complexity: O(1) since we are not using any extra space

# Test cases
# 1 -> 4 -> 5
# 1 -> 3 -> 4
# 2 -> 6
# Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

s = Solution()

result = s.mergeKLists([node1, node2, node3])

assert result.val == 1
assert result.next.val == 1
assert result.next.next.val == 2
assert result.next.next.next.val == 3
assert result.next.next.next.next.val == 4
assert result.next.next.next.next.next.val == 4
assert result.next.next.next.next.next.next.val == 5
assert result.next.next.next.next.next.next.next.val == 6
assert result.next.next.next.next.next.next.next.next == None

while result:
    print(result.val)
    result = result.next

print("All test cases passed!")
