# Recursion

## Recursion (One Branch)

Recursion can be a difficult concept to wrap your head around so don't be discouraged if you don't understand it right away.

Simply put, recursion is when a function calls itself, usually with a different input. This is known as a recursive function.

Recursive functions can be thought of as functions that breaks down a problem into smaller sub-problems and solves them in reverse order. It's usually possible to convert a recursive function into an iterative one, and vice versa.

For some problems an iterative solution can be much more simple to implement than a recursive one, and vice versa.
Recursive functions have two parts:

1. The base case.
2. The recursive case.

The concept of recursion applies to the real world as well. Consider a box that contains another box, which contains another box, and so on. This is a recursive structure.

In this case, the base case would be the smallest box, and the recursive case would be the larger boxes that contain the smaller boxes.

### Time and Space Complexity

#### Time: O(n)

-   In total, n calls are being made to the factorial function, where each function call is O(1), making the total time complexity O(n).

#### Space: O(n)

-   While we aren't using any data structures, recursion operates off of an implicit stack, known as the function call stack. That is how we are able to return from one function call to the previous one. Since there are n recursive calls, there will be n function calls placed on the stack, which results in O(n) space.

## Recursion (Two Branch)

A more common case of recursion is multi-branch recursion. In this lesson we will attempt to solve the Fibonacci sequence problem using two-branch recursion.

The Fibonacci sequence is a set of numbers that starts with a one or a zero, followed by a one, and proceeds based on the rule that each number is equal to the sum of the preceding two numbers.

The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The Fibonacci sequence can be defined as follows:

-   F(0) = 0
-   F(1) = 1
-   F(n) = F(n-1) + F(n-2)

Let's implement the Fibonacci sequence using two-branch recursion.

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
print(fibonacci(5)) # Output: 5
print(fibonacci(10)) # Output: 55
```

In the code snippet above, we have a function `fibonacci` that takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence.

### Time and Space Complexity

#### Time: O(2^n)

-   The time complexity of the Fibonacci sequence using two-branch recursion is O(2^n). This is because for each number in the sequence, two recursive calls are made.

#### Space: O(n)

-   The space complexity of the Fibonacci sequence using two-branch recursion is O(n). This is because the function call stack will contain at most n function calls.
