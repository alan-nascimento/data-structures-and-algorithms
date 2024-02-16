# Explanation for Question 1

In this code, I've used a singly linked list to implement the data structure. A linked list was chosen because it allows for dynamic memory allocation and efficient insertion and deletion operations, which are common in scenarios involving sets of data. Each node in the linked list holds a value and a reference to the next node. This allows for straightforward traversal of the list.

## Time Efficiency:

- Appending to the end of the linked list (`append` method) takes O(n) time, where n is the number of elements in the list. This is because it requires traversing the entire list to find the last node.
- Finding the size of the linked list (`size` method) also takes O(n) time since it requires traversing the entire list to count the number of nodes.
- Finding the union and intersection of two linked lists (`union` and `intersection` functions) involves traversing each list once and adding elements to a set. Set operations like addition, intersection, and union typically have an average time complexity of O(1) for each operation.

## Space Efficiency:

- The space efficiency of this solution is determined by the additional space required for storing unique elements in sets during union and intersection operations. Since sets in Python are implemented using hash tables, the space complexity for adding elements to sets is typically O(n), where n is the number of unique elements.
- The space complexity of the linked list itself is O(n), where n is the number of elements in the list, as it requires allocating memory for each node.
