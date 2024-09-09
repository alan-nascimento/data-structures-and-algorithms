# Linked Lists

A linked list is another data structure that is like an array in the sense that it stores elements in an ordered sequence. But there are also some key differences.

The main difference is that linked lists are made up of objects called ListNode's. This object contains two attributes:

value - This stores the value of the node. It could be a character, an integer, etc.
next - This stores the reference to the next node in the linked list. The picture below visualizes the ListNode object.

## Singly Linked Lists

In a singly linked list, each node has a reference to the next node in the sequence. The first node is called the head and the last node is called the tail. The tail node points to null, indicating the end of the linked list.

## Doubly Linked Lists

As the name implies, each node now has two pointers. In addition to the next pointer, we have a prev pointer which points to the previous node. If the prev pointer points to null, it is an indication that we are at the head of the linked list.

Similar to the singly linked list, adding a node to a doubly linked list will run in O(1) time. Only this time, we have to update the prev pointer as well.

Similar to singly linked lists, we cannot randomly access a node. So in the worst case, we will have to traverse n nodes before reaching the desired node. This would run in O(n) time.

Doubly linked lists have the benefit that we can traverse the list in both directions, as opposed to singly linked lists.
