# Bit Manipulation Overview

## Introduction

**Bit manipulation** refers to the act of algorithmically working on bits within a binary representation of numbers. Since computers store data in binary format (0s and 1s), bit manipulation allows for efficient and low-level operations, often leading to faster computations compared to traditional arithmetic operations. These operations are frequently used in competitive programming, graphics, cryptography, and system-level programming.

The key operations in bit manipulation include AND, OR, XOR, NOT, shifts, and more. By mastering bit manipulation, you can perform various tasks like toggling bits, checking if numbers are even or odd, or finding the unique element in a collection in constant time.

## Key Bitwise Operators

Bit manipulation involves several key operators:

-   **AND (`&`)**: Returns 1 only if both bits are 1.
    -   Example: `5 & 3` (`0101 & 0011`) = `0001` (1 in decimal).
-   **OR (`|`)**: Returns 1 if either of the bits is 1.
    -   Example: `5 | 3` (`0101 | 0011`) = `0111` (7 in decimal).
-   **XOR (`^`)**: Returns 1 if the bits are different.
    -   Example: `5 ^ 3` (`0101 ^ 0011`) = `0110` (6 in decimal).
-   **NOT (`~`)**: Flips the bits (1 becomes 0, and 0 becomes 1).
    -   Example: `~5` (`~0101`) = `1010` (two's complement representation).
-   **Left Shift (`<<`)**: Shifts the bits to the left by a specified number of positions, filling with 0s.
    -   Example: `5 << 1` (`0101 << 1`) = `1010` (10 in decimal).
-   **Right Shift (`>>`)**: Shifts the bits to the right by a specified number of positions. For signed integers, this maintains the sign bit.
    -   Example: `5 >> 1` (`0101 >> 1`) = `0010` (2 in decimal).

## Common Bit Manipulation Techniques

### 1. Checking if a Number is Even or Odd

To check whether a number is even or odd, you can use the bitwise AND operator with 1.

```python
def is_odd(n):
    return n & 1 == 1

# Example usage
is_odd(5)  # True
is_odd(4)  # False
```

### 2. Swapping Two Numbers Without a Temporary Variable

You can swap two numbers using XOR without needing a temporary variable.

```python
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Example usage
swap(5, 7)  # (7, 5)
```

### 3. Counting the Number of 1s in a Binary Representation (Hamming Weight)

This can be done efficiently using bit manipulation by continuously clearing the least significant 1-bit until the number becomes zero.

```python
def count_ones(n):
    count = 0
    while n:
        n &= (n - 1)  # Clears the least significant bit set to 1
        count += 1
    return count

# Example usage
count_ones(5)  # 2 (since 5 in binary is 101)
```

### 4. Checking if a Number is a Power of Two

A number is a power of two if it has exactly one bit set to 1. This can be checked using:

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example usage
is_power_of_two(8)  # True (since 8 in binary is 1000)
is_power_of_two(10)  # False
```

### 5. Getting the ith Bit of a Number

To extract the ith bit of a number, you can use a combination of shift and AND operations.

```python
def get_ith_bit(n, i):
    return (n >> i) & 1

# Example usage
get_ith_bit(5, 2)  # 1 (since 5 in binary is 101, the 2nd bit is 1)
```

### 6. Set the ith Bit of a Number

To set the ith bit of a number, use the bitwise OR with a mask where the ith bit is set to 1.

```python
def set_ith_bit(n, i):
    return n | (1 << i)

# Example usage
set_ith_bit(5, 1)  # 7 (since setting the 1st bit of 5 (101) results in 111)
```

### 7. Clear the ith Bit of a Number

To clear the ith bit, use the bitwise AND with a mask that has all bits set to 1 except the ith bit.

```python
def clear_ith_bit(n, i):
    return n & ~(1 << i)

# Example usage
clear_ith_bit(5, 2)  # 1 (since clearing the 2nd bit of 5 (101) results in 001)
```

### 8. Toggle the ith Bit of a Number

To toggle (invert) the ith bit, use XOR with a mask where only the ith bit is 1.

```python
def toggle_ith_bit(n, i):
    return n ^ (1 << i)

# Example usage
toggle_ith_bit(5, 2)  # 1 (since toggling the 2nd bit of 5 (101) results in 001)
```

## Practical Applications

1. **Fast Algorithms**: Bit manipulation is frequently used in algorithms where speed is critical, such as cryptographic algorithms and encoding/decoding techniques.

2. **Efficient Space Use**: It allows you to manipulate data using minimal memory, such as in bit-level compression, or storing multiple boolean values in a single integer.

3. **Competitive Programming**: Many problems in competitive programming involve bit manipulation techniques for fast computation, like subset generation or solving XOR-based problems.

4. **Low-Level System Programming**: Bit manipulation is widely used in system programming for working with hardware registers, protocol flags, and permissions.

## Conclusion

Bit manipulation is a powerful and efficient way to operate directly on binary data. Mastering bitwise operations can lead to performance improvements in algorithms and a deeper understanding of how computers process data at a low level. By learning these techniques, you can solve a wide range of problems more efficiently, especially in cases that involve binary numbers, masks, and low-level data structures.

### References:

-   [Bitwise Operations](https://en.wikipedia.org/wiki/Bitwise_operation)
-   [XOR Swap Algorithm](https://en.wikipedia.org/wiki/XOR_swap_algorithm)
