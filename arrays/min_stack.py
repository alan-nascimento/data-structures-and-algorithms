class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if len(self.min_stack) > 0 else val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Time complexity is 𝑂(1) for all operations
# Space complexity is 𝑂(𝑛) where n is the number of elements in the stack

# This solution ensures constant-time operations for all stack-related methods, but the trade-off is that we use 𝑂(𝑛) additional space for the minStack

# Test cases
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
assert min_stack.getMin() == -3
print(min_stack.getMin()) # -3
min_stack.pop()
assert min_stack.top() == 0
print(min_stack.top()) # 0
assert min_stack.getMin() == -2
print(min_stack.getMin()) # -2

print("All test cases passed!")
