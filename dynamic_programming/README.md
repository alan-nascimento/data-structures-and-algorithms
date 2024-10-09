# Dynamic Programming (DP) Overview

## Introduction

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is particularly effective when a problem exhibits **overlapping subproblems** and **optimal substructure**. In DP, we store the results of subproblems to avoid recalculating them, thus saving time and improving efficiency. Problems solved using DP typically involve optimizing a certain value, such as minimizing cost or maximizing a score.

## Key Concepts

-   **Overlapping Subproblems**: The problem can be divided into subproblems, which are reused several times. This allows us to store the solutions to these subproblems for future reference.

-   **Optimal Substructure**: The solution to the original problem can be composed of optimal solutions to its subproblems.

There are two main approaches to implementing dynamic programming:

1. **Top-Down (Memoization)**: This approach solves the problem recursively and stores the results of subproblems in a memoization table to avoid redundant calculations.
2. **Bottom-Up (Tabulation)**: In this approach, the solution is built iteratively, starting from the simplest subproblems and combining their results to solve the larger problem.

## Dynamic Programming Example: Fibonacci Sequence

One of the simplest examples of DP is calculating the Fibonacci numbers:

```
fib(n) = fib(n-1) + fib(n-2)
```

### Fibonacci Solution Using Bottom-Up DP:

```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## 2D Dynamic Programming (2D DP)

2D Dynamic Programming is used when the problem involves two dimensions, i.e., two variables affecting the state of the solution. This often happens in grid-based problems, string matching, and sequence comparison.

### Key Concepts in 2D DP:

-   The **DP table** is a two-dimensional array, where each cell `dp[i][j]` stores the result of a subproblem defined by two parameters `i` and `j`.
-   You fill this DP table by solving subproblems iteratively (bottom-up) or recursively (top-down), ensuring that previously computed results are reused.

### Example Problem: Longest Common Subsequence (LCS)

Given two strings `X` and `Y`, find the length of their longest common subsequence.

### LCS Solution Using 2D DP:

```python
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
```

In this example:

-   The DP table `dp[i][j]` stores the length of the LCS for the substrings `X[0..i-1]` and `Y[0..j-1]`.
-   The final solution is found in `dp[m][n]`, where `m` and `n` are the lengths of the two input strings.

### Typical Use Cases for 2D DP:

1. **Grid-based problems**: Calculating the minimum or maximum path sum in a grid.
2. **String comparison**: Problems like the longest common subsequence or edit distance between two strings.
3. **Knapsack-like problems**: Problems where you have to make optimal choices based on two varying parameters, such as capacity and item properties.

## General Steps to Implement DP:

1. **Define the State**: Clearly define what the state `dp[i]` (or `dp[i][j]` in 2D DP) represents.
2. **Recurrence Relation**: Derive how the current state depends on previous states.
3. **Base Case**: Identify the initial conditions for the smallest subproblems.
4. **Solve Iteratively or Recursively**: Use either a bottom-up iterative approach or a top-down recursive approach with memoization.

## Conclusion

Dynamic Programming is a powerful technique for solving optimization and decision-making problems. By storing the results of smaller subproblems, DP can significantly reduce time complexity. Whether using 1D DP for sequence-based problems or 2D DP for more complex, multi-variable problems, the approach is based on the same principles of breaking down the problem and solving it incrementally.

### References:

-   [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
-   [Longest Common Subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)
