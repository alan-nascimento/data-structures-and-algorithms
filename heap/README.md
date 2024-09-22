# Heap Properties

A heap is a specialized, tree-based data structure.

It implements an abstract data type called the Priority Queue, but sometimes 'Heap' and 'Priority Queue' are used interchangeably.

We already learned that queues operate with a first-in-first-out basis but with a priority queue, the values are removed based on a specific priority. The element with the highest priority is removed first, regardless of the order in which it was added.

## Two types of heaps

-   Min Heap
-   Max Heap

Min heaps have the smallest value at the root node. The smallest value has the highest priority to be removed.

Max heaps have the largest value at the root node. The largest value has the highest priority to be removed.

In this lesson, we will be focusing on min heaps, but the implementation is exactly the same for max heap, except you would prioritize the maximum value instead of the minimum.

## Heap Properties

For a binary tree to qualify as a heap, it must satisfy the following properties:

1. Structure Property
   A binary heap is a binary tree that is a complete binary tree, where every single level of the tree is filled completely, except possibly the lowest level nodes, which are filled contiguously from left to right.

2. Order Property

The order property for a min-heap is that all of the descendents should be greater than their ancestors. In other words, if we have a root with value y, every node in the right and the left sub-tree should have values greater than or equal to y. This is a recursive property, similar to binary search trees.

In a max-heap, every node in the right and the left sub-tree is smaller than or equal to y.

Unlike binary search trees, heaps may contain duplicate values.

## Heaps Push and Pop

With heaps we can read the minimum or maximum value in constant time, O(1) by simply reading the element at the first position.

However, pushing and popping from a heap is more complicated, but can still be accomplished efficiently with a time complexity of O(log n).

## Push

When we push a new element into a heap, we add it to the end of the heap and then we "bubble up" the element to its correct position.

## Pop

When we pop an element from a heap, we remove the root element and replace it with the last element in the heap. We then "bubble down" the element to its correct position.

## Heapify

Heapify is a process of converting a binary tree into a heap. This is done by starting at the last parent node and bubbling down to the root node.

## Conclusion

Heaps are a powerful data structure that can be used to implement priority queues. They are efficient for finding the minimum or maximum value in constant time, and for pushing and popping elements in logarithmic time.
