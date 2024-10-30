## Kadane's Algorithm

Kadane's algorithm is a greedy/dynamic programming algorithm that can be used on an array. It is used to calculate the maximum sum subarray ending at a particular position and typically runs in O(n) time complexity.

### Motivation

Given an array of integers, we want to find the contiguous subarray with the largest sum. This is a classic problem that can be solved using Kadane's algorithm.

### Algorithm

1. Initialize two variables `max_so_far` and `max_ending_here` to 0.
2. Iterate over the array.
3. For each element, update `max_ending_here` to the maximum of the current element and the sum of the current element and `max_ending_here`.
4. Update `max_so_far` to the maximum of `max_so_far` and `max_ending_here`.
5. Return `max_so_far`.

### Example

Given an array `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the maximum sum subarray is `[4, -1, 2, 1]` with a sum of `6`.

### Implementation

```python
def kadanes_algorithm(arr):
    max_so_far = max_ending_here = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

### Complexity

-   Time complexity: O(n)
-   Space complexity: O(1)
