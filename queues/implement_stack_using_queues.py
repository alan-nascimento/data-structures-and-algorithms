from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

# Time Complexity: O(n) for pop, O(1) for top and empty
# Space Complexity: O(n) where n is the number of elements in the stack

# Test cases

stack = MyStack()

# Test 1

stack.push(1)
stack.push(2)
assert stack.top() == 2

# Test 2

assert stack.pop() == 2
assert stack.empty() == False

print("All tests passed!")
