# Binary Search Trees

## Binary Tree

A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

Similar to linked lists, binary trees are another data structure that involve nodes and pointers.

With linked lists, we connected nodes in a straight line with next and prev pointers. Nodes in a binary tree also have at most two pointers, but we call them the left child and the right child pointers. The first node in a binary tree is referred to as the root node. We draw the pointers down instead of a straight line.

The value of a node can be any data type. A TreeNode class would look like the following. Notice how much of the implementation is similar to a ListNode discussed in the linked list chapter, except these nodes are considered children.

### Root Node

Root node is the highest node in the tree and has no parent node. All of the nodes in the tree can be reached by the root node.

Binary Search Trees (BST) are a variation of binary trees with the addition of a sorted property. The property is that every node in the left subtree is smaller than the root and every node in the right subtree is greater than the root.

### Leaf Nodes

Leaf nodes are nodes with no children. The nodes at the last level of the tree are guaranteed to be leaf nodes but they can also be found on other levels.

## Binary Search Tree

A binary search tree is a binary tree in which every node fits a specific ordering property: all left descendants <= n < all right descendants.

## Operations

-   `insert(value)`: inserts a new node with the given value in the binary search tree.
-   `search(value)`: searches for a node with the given value in the binary search tree.
-   `delete(value)`: deletes a node with the given value from the binary search tree.
-   `inorder()`: prints the values of the nodes in the binary search tree using inorder traversal.
-   `preorder()`: prints the values of the nodes in the binary search tree using preorder traversal.
-   `postorder()`: prints the values of the nodes in the binary search tree using postorder traversal.

## BST Insert and Remove

-   Insertion: O(log n)
-   Removal: O(log n)

## Depth-First Search (DFS)

Depth First Search (DFS) is one of the most common algorithms in coding interviews. It is commonly used to traverse trees and graphs. In this lesson we will focus on trees.

If we want to traverse an entire tree, we have to visit every node. One way to accomplish this is by using depth-first search.

The idea is we pick a direction, say left, and keep following pointers as far down left as we can go until we reach null. Once we reach null, we backtrack to the parent node and then go right. We keep doing this until we have visited every node in the tree. This is the essence of depth-first search.

As the name implies, we go as deep as possible before we backtrack.

There are three ways to traverse a tree using depth-first search:

-   Inorder: left, root, right
-   Preorder: root, left, right
-   Postorder: left, right, root

## Breadth-First Search (BFS)

In depth-first search, we prioritized depth. For breath-first search (BFS), we prioritize breadth, meaning we focus on visiting all the nodes on one level before moving on to the next level.

BFS is also known as level-order traversal when referring to trees, since we visit the nodes level by level.

enerally, breadth-first search is implemented iteratively and that is the implementation we will be covering in this course.

Since we want to visit all the nodes on one level before moving to the next, we will need a data structure that allows us to do this.

A queue data structure, more specifically, a deque, allows us to remove elements both from the head and the tail in O(1) time. For BFS we will append elements to the tail and remove elements from the head as we go through each level of the tree from left to right.

## BST Sets and Maps

Sets and Maps, similar to stacks and queues, are interfaces that can be implemented using trees. Implementing them with trees allows for a O(log n) time for insertion, deletion, and search operations.

### Sets

Imagine we have a phone book with three names - Alice, Brad, Collin. We could store these using dynamic arrays but a set ensures that we have unique values in our data structure, and implementing it using a tree ensures that our keys are sorted alphabetically. This is known as a TreeSet.

### Maps

A map on the other hand operates on key-value pair. If implemented with a tree, it is commonly referred to as a TreeMap.

Going back to our phone book example, not only can we store names, but also map them to their phone numbers. Again, the data structure is sorted by the key. Because the key maps to a value, we can find all of the information associated with a key.

In this example, the key may be the last name of the person. The value here doesn't have to be a phone number, it can also be an object or another data type. The only requirement is that we can compare keys to each other, since the trees must follow some sort of order.

## Conclusion

Binary search trees are a powerful data structure that can be used to implement sets and maps. They are also used to implement priority queues and are the foundation for more advanced data structures like AVL trees and red-black trees.
