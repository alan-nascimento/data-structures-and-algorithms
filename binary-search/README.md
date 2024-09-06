# Binary Search

Binary search is an efficient way of searching for elements within a sorted array. Typically we are given an array, and a target element to search for.

The idea behind binary search is similar to how we would search for a word in a dictionary. We would open the dictionary in the middle and determine if the word we are looking for is in the left or right half. We would then repeat this process until we find the word or determine that it doesn't exist in the dictionary.

Similarly, binary search divides a given array by the middle index, called mid and compares the value at mid to the target value. If the target is greater than the mid value, we will search the right half of the array. If the target is less than the mid value, we will search the left half of the array.

In interviews and algorithmic problems, there are two common variations of binary search problems:

1. Search Array - a sorted array, and a target is given and the task is to determine if the target is found in the array.
2. Search Range - a range of numbers is given rather than an array, without a specific target.

## Search Array

### Implementation

Binary search can be implemented using either an iterative or recursive approach. The iterative approach is more common and is generally preferred due to the reduced overhead of function calls.

The iterative approach involves initializing two pointers, `left` and `right`, which represent the start and end of the array. We then calculate the mid index and compare the value at mid to the target. If the target is found, we return the index. If the target is less than the mid value, we update the right pointer to mid - 1. If the target is greater than the mid value, we update the left pointer to mid + 1.

The process is repeated until the left pointer is greater than the right pointer, at which point we return -1 to indicate that the target was not found.

### Complexity Analysis

The time complexity of binary search is O(log n) where n is the number of elements in the array. This is because the search space is halved at each step.

The space complexity of binary search is O(1) since we are using a constant amount of space.

## Search Range

Imagine you picked a number from 1 - 100 and asked your friend to guess the number you were thinking of. There are three outcomes. Either their guess is correct, too small or too large.

After every guess, you would tell them if their guess was correct, too small or too large. Your friend would then adjust their next guess accordingly.

This is the concept behind the search range problem. We are given a range of numbers and asked to guess a number within that range. After each guess, we are told if our guess is correct, too small or too large.

### Implementation

The search range problem can be implemented using binary search. We initialize two pointers, `left` and `right`, which represent the start and end of the range. We then calculate the mid index and guess the number at mid. If the guess is correct, we return the mid index. If the guess is too small, we update the left pointer to mid + 1. If the guess is too large, we update the right pointer to mid - 1.

The process is repeated until the left pointer is greater than the right pointer, at which point we return -1 to indicate that the number was not found.

### Complexity Analysis

The time complexity of the search range problem is O(log n) where n is the size of the range. This is because the search space is halved at each step.

The space complexity of the search range problem is O(1) since we are using a constant amount of space.

## Summary

Binary search is an efficient way of searching for elements within a sorted array. It is a common algorithmic problem and can be implemented using either an iterative or recursive approach. The time complexity of binary search is O(log n) and the space complexity is O(1).
