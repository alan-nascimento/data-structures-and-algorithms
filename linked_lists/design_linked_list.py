class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        currentIndex = 0

        while currentIndex < index:
            current = current.next
            currentIndex += 1

        return current.val

    def getNode(self, index: int) -> ListNode:
        if index < 0 or index >= self.size:
            return None

        current = self.head
        currentIndex = 0

        while currentIndex < index:
            current = current.next
            currentIndex += 1

        return current

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        newNode = ListNode(val)
        currentNode = self.getNode(index)

        if currentNode:
            newNode.prev = currentNode.prev
            newNode.next = currentNode
            if currentNode.prev:
                currentNode.prev.next = newNode
            currentNode.prev = newNode

        if index == 0:
            self.head = newNode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None

        currentNode = self.getNode(index)

        if currentNode:
            if currentNode.prev:
                currentNode.prev.next = currentNode.next
            else:
                self.head = currentNode.next

            if currentNode.next:
                currentNode.next.prev = currentNode.prev
            else:
                self.tail = currentNode.prev

            self.size -= 1

# Test cases
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
print("-------------------")
print(myLinkedList.get(0))
myLinkedList.addAtTail(3)
print("-------------------")
print(myLinkedList.get(0))
print(myLinkedList.get(1))
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
print("-------------------")
print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2))
myLinkedList.get(1)              # return 2
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
print("-------------------")
print(myLinkedList.get(0))
print(myLinkedList.get(1))
myLinkedList.get(1)              # return 3
