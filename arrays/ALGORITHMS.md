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

## Sliding Window Technique

The sliding window technique is used to solve problems where we need to find a subarray that meets certain conditions. It involves maintaining a window that can slide over the array and is used to track the subarray that meets the conditions.

### Motivation

Given an array of integers and a target sum, we want to find the minimum subarray length that has a sum greater than or equal to the target sum. This is a classic problem that can be solved using the sliding window technique.

### Algorithm

1. Initialize two pointers `left` and `right` to 0.
2. Initialize a variable `min_length` to infinity.
3. Iterate over the array using the `right` pointer.
4. Update the window sum by adding the element at the `right` pointer.
5. While the window sum is greater than or equal to the target sum, update `min_length` and shrink the window by moving the `left` pointer.
6. Return `min_length`.

### Example

Given an array `[2, 3, 1, 2, 4, 3]` and a target sum of `7`, the minimum subarray length with a sum greater than or equal to `7` is `2` (the subarray `[4, 3]`).

### Implementation

```python
def min_subarray_length(arr, target_sum):
    left = 0
    window_sum = 0
    min_length = float('inf')
    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= target_sum:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1
    return min_length if min_length != float('inf') else 0
```

### Complexity

-   Time complexity: O(n)
-   Space complexity: O(1)
